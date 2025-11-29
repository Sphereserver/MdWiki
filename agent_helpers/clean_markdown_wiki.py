#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clean & normalize converted MediaWiki Markdown files (Sphere-ready).

Main features:
- Recursively process .md files in a tree.
- Remove MediaWiki magic words like __FORCETOC__.
- Convert HTML tables (<table>, <tr>, <td>, <th>, <tbody>) to aligned Markdown tables.
- Convert <ul>/<li> to Markdown bullet lists.
- Convert inline HTML (<strong>, <em>, <a>, <p>, <div>, <span>) to Markdown or strip layout tags.
- Normalize / repair malformed Markdown tables; keep total width <= MAX_TABLE_WIDTH.
- Preserve internal whitespace; trim only trailing spaces.
- SphereScript highlighting:
  - Wraps identifiers with given prefixes in backticks: TAG., T_, DEF., etc.
  - Wraps control-flow keywords (IF/ENDIF, WHILE/ENDWHILE, FOR*/ENDFOR, DOSWITCH/ENDDO).
  - Wraps square-bracket blocks [ ... ].
- Colorized unified diff with clear separators and extra spacing.

Usage:
    python3 clean_markdown_wiki.py /path/to/root
    python3 clean_markdown_wiki.py /path --spherescript-prefixes TAG. T_ DEF. DEF0.
"""

import argparse
import difflib
import re
import sys
from pathlib import Path
from typing import List, Match

# ---------------------------------------------------------------------------
# Global constants
# ---------------------------------------------------------------------------

# Maximum total width (in characters) for a Markdown table row,
# including leading/trailing pipes and spaces.
MAX_TABLE_WIDTH = 100

# Default SphereScript prefixes for highlighting (case-insensitive).
DEFAULT_SPHERESCRIPT_PREFIXES = [
    "TAG.", "TAG0.", "T_", "DEF.", "DEF0.", "DEFMSG.", "DEFMSG0.",
    "CTAG.", "CTAG0.", "VAR.", "VAR0.", "LIST.", "SERV.", "I.",
    "SRC.", "NEW.", "ON=", "RETURN",
]

# MediaWiki magic words to remove
MEDIAWIKI_MAGIC_WORDS = [
    "__FORCETOC__", "__NOTOC__", "__TOC__", "__NOEDITSECTION__",
    "__NEWSECTIONLINK__", "__NONEWSECTIONLINK__", "__NOGALLERY__",
]

# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean MediaWiki-converted Markdown.")
    parser.add_argument("root", help="Root directory containing Markdown files.")
    parser.add_argument(
        "--spherescript-prefixes",
        nargs="*",
        default=DEFAULT_SPHERESCRIPT_PREFIXES,
        help=(
            "SphereScript identifier prefixes to highlight with backticks. "
            "Example: TAG. T_ DEF. DEF0. (case-insensitive)"
        ),
    )
    return parser.parse_args()

# ---------------------------------------------------------------------------
# Generic helpers
# ---------------------------------------------------------------------------

def remove_mediawiki_magic(text: str) -> str:
    """Remove MediaWiki magic words like __FORCETOC__ from the text."""
    for word in MEDIAWIKI_MAGIC_WORDS:
        text = text.replace(word, "")
    return text

def normalize_spacing_safely(text: str) -> str:
    """
    Only trim trailing whitespace on each line.
    Preserve leading whitespace and internal spacing entirely.
    """
    lines = [line.rstrip() for line in text.splitlines()]
    result = "\n".join(lines)
    # Ensure a single trailing newline if file is non-empty
    if result and not result.endswith("\n"):
        result += "\n"
    return result

# ---------------------------------------------------------------------------
# Markdown escaping
# ---------------------------------------------------------------------------

def escape_md_special_chars(text: str) -> str:
    """
    Escape Markdown special characters in table cells / inline text where needed.

    Characters escaped:
    - *   (bold/italics marker)
    - `   (code span marker)
    - [ ] (link / reference brackets)
    - \   (backslash)
    - ( ) (link target)
    - # + - > (list / heading markers)
    - |   (table cell separator)
    """
    special_chars = r'*`\[\]\\()#+->|'
    # Replace any occurrence of these chars with a backslash-escaped version.
    return re.sub(rf"[{re.escape(special_chars)}]", lambda m: "\\" + m.group(0), text)

# ---------------------------------------------------------------------------
# Inline HTML → Markdown
# ---------------------------------------------------------------------------

def convert_inline_html(text: str) -> str:
    """
    Convert common inline HTML tags to Markdown equivalents, preserving
    existing Markdown syntax.

    1. <strong>, <b> → **text**
    2. <em>, <i>     → *text*
    3. <a href="url">label</a> → [label](url)
    4. Strip layout <div>, <span> but keep their content.
    5. <p> is handled in table cells separately; here we only clean generic cases.
    """

    # 1. <strong> or <b> to **...**
    def strong_replacer(m: Match) -> str:
        # group(2) = content between tags
        return f"**{m.group(2).strip()}**"

    text = re.sub(
        r"<\s*(strong|b)\b[^>]*>(.*?)</\s*(strong|b)\s*>",
        strong_replacer,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 2. <em> or <i> to *...*
    def em_replacer(m: Match) -> str:
        return f"*{m.group(2).strip()}*"

    text = re.sub(
        r"<\s*(em|i)\b[^>]*>(.*?)</\s*(em|i)\s*>",
        em_replacer,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 3. <a href="url">text</a> to [text](url)
    def link_replacer(m: Match) -> str:
        url = m.group(1).strip()
        label = m.group(2).strip()
        if not label:
            label = url
        return f"[{label}]({url})"

    text = re.sub(
        r'<\s*a\b[^>]*href\s*=\s*"([^"]*)"[^>]*>(.*?)</\s*a\s*>',
        link_replacer,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 4. Remove layout <div> / <span> but keep inner text
    text = re.sub(r"<\s*(div|span)\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</\s*(div|span)\s*>", "", text, flags=re.IGNORECASE)

    return text

# ---------------------------------------------------------------------------
# HTML tables → Markdown tables
# ---------------------------------------------------------------------------

def cleanup_cell_content(s: str) -> str:
    """
    Clean content inside table cells.

    Steps:
    - Strip outer whitespace.
    - Remove table structure tags: <tbody>, <tr>, <td>, <th>.
    - Remove nested <p> wrappers, keeping the inner text.
    - Run inline HTML conversion for strong/em/links.
    - Normalize <br> variants to <br />.
    - Collapse multiple blank lines inside the cell.
    - Escape Markdown special chars that break cells.
    """
    s = s.strip()

    # Remove table-structure tags (both opening and closing)
    s = re.sub(r"</?tbody[^>]*>", "", s, flags=re.IGNORECASE)
    s = re.sub(r"</?(tr|td|th)\b[^>]*>", "", s, flags=re.IGNORECASE)

    # Remove <p> wrappers around cell content
    s = re.sub(
        r"<\s*p\b[^>]*>(.*?)</\s*p\s*>",
        lambda m: m.group(1).strip(),
        s,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Convert inner inline HTML (strong/em/a/div/span)
    s = convert_inline_html(s)

    # Normalize <br> tags
    s = re.sub(r"<\s*br\s*/?\s*>", "<br />", s, flags=re.IGNORECASE)

    # Collapse excessive blank lines inside cell
    s = re.sub(r"\n\s*\n+", "\n", s)

    # Escape problematic Markdown chars for tables
    s = escape_md_special_chars(s)

    return s.strip()

def convert_html_tables_to_markdown(text: str) -> str:
    """
    Convert all HTML <table>...</table> blocks to Markdown tables.

    For each table:
    - Extract <tr> rows.
    - Extract <th> or <td> cells from each row.
    - Compute natural column widths from content.
    - If total row width exceeds MAX_TABLE_WIDTH, scale all columns down
      proportionally to keep the total ≤ MAX_TABLE_WIDTH.
    - Emit all rows (header + body) with space-padded cells so every row
      has the same physical width.
    """

    def convert_single_table(m: Match) -> str:
        table_html = m.group(0)

        # Extract all <tr>...</tr> rows
        rows_html = re.findall(
            r"<\s*tr\b[^>]*>(.*?)</\s*tr\s*>",
            table_html,
            flags=re.IGNORECASE | re.DOTALL,
        )

        parsed_rows: List[List[str]] = []

        for row_html in rows_html:
            # Recursively convert nested tables before handling cells
            row_html = convert_html_tables_to_markdown(row_html)

            # Prefer header cells <th> first
            th_cells = re.findall(
                r"<\s*th\b[^>]*>(.*?)</\s*th\s*>",
                row_html,
                flags=re.IGNORECASE | re.DOTALL,
            )
            if th_cells:
                cells = th_cells
            else:
                cells = re.findall(
                    r"<\s*td\b[^>]*>(.*?)</\s*td\s*>",
                    row_html,
                    flags=re.IGNORECASE | re.DOTALL,
                )

            cleaned_cells = [cleanup_cell_content(c) for c in cells]
            if cleaned_cells:
                parsed_rows.append(cleaned_cells)

        if not parsed_rows:
            # Could not parse as a simple table; keep original HTML
            return table_html

        # Determine number of columns
        max_cols = max(len(row) for row in parsed_rows) or 1

        # Compute natural widths per column
        col_widths = [0] * max_cols
        for row in parsed_rows:
            for col_idx, cell in enumerate(row):
                if col_idx < max_cols:
                    col_widths[col_idx] = max(col_widths[col_idx], len(cell))

        # Compute total row width including pipes and spaces.
        # Each column contributes: 1 leading space + content + 1 trailing space + 1 pipe.
        # For N columns: sum(widths) + 3*N + 1 (leftmost '|').
        total_width = sum(col_widths) + max_cols * 3 + 1

        if total_width > MAX_TABLE_WIDTH:
            # Scale columns down proportionally (keeping at least width 1).
            scale_factor = MAX_TABLE_WIDTH / max(total_width, 1)
            col_widths = [max(1, int(w * scale_factor)) for w in col_widths]

        # Prepare header and body rows (pad with empty strings if needed)
        header = parsed_rows[0] + [""] * (max_cols - len(parsed_rows[0]))
        body_rows = [row + [""] * (max_cols - len(row)) for row in parsed_rows[1:]]

        md_lines: List[str] = []

        # Header row
        header_line = "|"
        for i, cell in enumerate(header):
            cell = cell[:col_widths[i]]  # truncate if scaling made width smaller
            padding = " " * (col_widths[i] - len(cell))
            header_line += f" {cell}{padding} |"
        md_lines.append(header_line)

        # Separator row (use dashes spanning the actual column width)
        sep_line = "|"
        for width in col_widths:
            sep_line += f" {'-' * width} |"
        md_lines.append(sep_line)

        # Body rows
        for row in body_rows:
            row_line = "|"
            for i, cell in enumerate(row):
                cell = cell[:col_widths[i]]
                padding = " " * (col_widths[i] - len(cell))
                row_line += f" {cell}{padding} |"
            md_lines.append(row_line)

        return "\n".join(md_lines)

    return re.sub(
        r"<\s*table\b[^>]*>.*?</\s*table\s*>",
        convert_single_table,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

# ---------------------------------------------------------------------------
# HTML lists → Markdown lists
# ---------------------------------------------------------------------------

def convert_html_lists_to_markdown(text: str) -> str:
    """
    Convert <ul>...</ul> + <li>...</li> into Markdown bullet lists.

    Each <li> becomes a line starting with "- ".
    Nested <ul> are not deeply indented here; they are flattened at the same level.
    """

    def convert_single_ul(m: Match) -> str:
        ul_html = m.group(0)
        li_items = re.findall(
            r"<\s*li\b[^>]*>(.*?)</\s*li\s*>",
            ul_html,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if not li_items:
            return ul_html

        md_items: List[str] = []
        for item in li_items:
            # Clean inline HTML inside list item
            cleaned = convert_inline_html(item).strip()
            if cleaned:
                md_items.append(f"- {cleaned}")

        return "\n".join(md_items)

    return re.sub(
        r"<\s*ul\b[^>]*>.*?</\s*ul\s*>",
        convert_single_ul,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

# ---------------------------------------------------------------------------
# Markdown table normalization / linting
# ---------------------------------------------------------------------------

def is_valid_md_table(lines: List[str]) -> bool:
    """
    Heuristic check whether a block of lines is already a valid Markdown table:
    - At least 2 lines (header + separator).
    - Header contains pipes.
    - Separator contains '-' and '|' characters.
    """
    if len(lines) < 2:
        return False
    header = lines[0].strip()
    separator = lines[1].strip()
    if "|" not in header:
        return False
    if "-" not in separator or "|" not in separator:
        return False
    return True

def normalize_single_table_block(block_lines: List[str]) -> List[str]:
    """
    Fix a malformed Markdown table and align columns.

    Steps:
    - Split rows into cell lists.
    - Compute per-column widths.
    - If total width exceeds MAX_TABLE_WIDTH, scale columns down proportionally.
    - Reconstruct header, separator, and rows with padded cells.
    """
    rows: List[List[str]] = [
        [p.strip() for p in line.split("|")[1:-1]]
        for line in block_lines
    ]
    if not rows:
        return block_lines

    max_cols = max(len(r) for r in rows) or 1
    col_widths = [0] * max_cols

    for row in rows:
        for col_idx, cell in enumerate(row):
            if col_idx < max_cols:
                col_widths[col_idx] = max(col_widths[col_idx], len(cell))

    total_width = sum(col_widths) + max_cols * 3 + 1
    if total_width > MAX_TABLE_WIDTH:
        scale_factor = MAX_TABLE_WIDTH / max(total_width, 1)
        col_widths = [max(1, int(w * scale_factor)) for w in col_widths]

    header = rows[0] + [""] * (max_cols - len(rows[0]))
    normalized: List[str] = []

    # Header
    header_line = "|"
    for i, cell in enumerate(header):
        cell = cell[:col_widths[i]]
        padding = " " * (col_widths[i] - len(cell))
        header_line += f" {cell}{padding} |"
    normalized.append(header_line)

    # Separator
    sep_line = "|"
    for width in col_widths:
        sep_line += f" {'-' * width} |"
    normalized.append(sep_line)

    # Body
    for row in rows[1:]:
        row_line = "|"
        padded_row = row + [""] * (max_cols - len(row))
        for i, cell in enumerate(padded_row):
            cell = cell[:col_widths[i]]
            padding = " " * (col_widths[i] - len(cell))
            row_line += f" {cell}{padding} |"
        normalized.append(row_line)

    return normalized

def normalize_md_tables(text: str) -> str:
    """
    Scan for Markdown tables and normalize only the malformed ones.
    Valid tables are preserved exactly as they are.
    """
    lines = text.splitlines()
    out_lines: List[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        # Potential table start: a line with '|' and the next line being a separator
        if "|" in line and i + 1 < n and "-" in lines[i + 1]:
            block_start = i
            while i < n and "|" in lines[i]:
                i += 1
            block_end = i
            block_lines = lines[block_start:block_end]

            if is_valid_md_table(block_lines):
                out_lines.extend(block_lines)
            else:
                fixed = normalize_single_table_block(block_lines)
                out_lines.extend(fixed)
        else:
            out_lines.append(line)
            i += 1

    return "\n".join(out_lines)

# ---------------------------------------------------------------------------
# SphereScript highlighting
# ---------------------------------------------------------------------------

def highlight_spherescript(text: str, prefixes: List[str]) -> str:
    """
    Highlight SphereScript constructs using backticks.

    1. Identifiers starting with configured prefixes (TAG., T_, DEF., etc.)
       → wrap the full word in backticks.
    2. Control-flow keywords at line start:
       IF, ELSEIF, ELSE, ENDIF,
       WHILE, ENDWHILE,
       FOR*, ENDFOR,
       DOSWITCH, ENDDO
       → wrap the keyword part in backticks.
    3. [ ... ] blocks (e.g. [DEFNAME]) → wrap the entire bracketed block in backticks.
    """

    # 1. Prefix-based identifiers
    # Build an alternation of prefixes like TAG\.|TAG0\.|T_
    prefixes_pattern = "|".join(re.escape(p.lower()) for p in prefixes)

    def prefix_replacer(m: Match) -> str:
        word = m.group(0)
        return f"`{word}`"

    # Regex explanation:
    # (?i)             : case-insensitive (we also set flags below)
    # \b               : word boundary
    # (prefixes...)+   : one of the known prefixes
    # [A-Za-z0-9_.]*   : the rest of the identifier
    text = re.sub(
        rf"\b({prefixes_pattern})[A-Za-z0-9_.]*",
        prefix_replacer,
        text,
        flags=re.IGNORECASE,
    )

    # 2. Control-flow keywords at the beginning of a line
    # FOR* (FOR, FORCHAR, FORITEM, etc.) is handled via FOR\w*
    cf_pattern = (
        r"^\s*(IF|ELSEIF|ELSE|ENDIF|WHILE|ENDWHILE|FOR\w*|ENDFOR|DOSWITCH|ENDDO)\b"
    )

    def control_flow_replacer(m: Match) -> str:
        full = m.group(0)
        keyword = m.group(1)
        # Replace only the first occurrence of the keyword inside the matched text
        return full.replace(keyword, f"`{keyword}`", 1)

    text = re.sub(
        cf_pattern,
        control_flow_replacer,
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    # 3. [ ... ] blocks → wrap whole [block] in backticks, e.g. `[DEFNAME]`
    def bracket_block_replacer(m: Match) -> str:
        block = m.group(0)
        return f"`{block}`"

    text = re.sub(
        r"\[[^\]\n]+\]",
        bracket_block_replacer,
        text,
        flags=re.MULTILINE,
    )

    return text

# ---------------------------------------------------------------------------
# Main processing pipeline
# ---------------------------------------------------------------------------

def process_markdown(text: str, spherescript_prefixes: List[str]) -> str:
    """
    Apply all cleanup and normalization steps to a single Markdown document.
    Order is important.
    """
    # 1. Remove MediaWiki magic
    text = remove_mediawiki_magic(text)

    # 2. SphereScript highlighting (identifiers, control flow, [blocks])
    text = highlight_spherescript(text, spherescript_prefixes)

    # 3. HTML lists (<ul>/<li>)
    text = convert_html_lists_to_markdown(text)

    # 4. HTML tables (<table>/<tr>/<td>/<th>/<tbody>)
    text = convert_html_tables_to_markdown(text)

    # 5. Inline HTML conversions (<strong>, <em>, <a>, <div>, <span>)
    text = convert_inline_html(text)

    # 6. Normalize malformed Markdown tables (alignment, width cap)
    text = normalize_md_tables(text)

    # 7. Trailing-whitespace cleanup (preserve internal whitespace)
    text = normalize_spacing_safely(text)

    return text

# ---------------------------------------------------------------------------
# Diff output
# ---------------------------------------------------------------------------

def show_diff(original: str, cleaned: str, path: Path) -> None:
    """
    Print a colorized unified diff for a file, with clear separators and spacing.

    - Cyan separators before/after each file's diff.
    - Green lines for additions, red lines for removals.
    - Ensure '---', '+++', and '@@' lines are each on their own line for readability.
    """
    orig_lines = original.splitlines(keepends=True)
    new_lines = cleaned.splitlines(keepends=True)

    # Leading blank line, then top cyan separator
    print()
    print("\033[36m" + "═" * 88 + "\033[0m")  # cyan
    print(f"\033[36mFile: {path}\033[0m")
    print("\033[36m" + "═" * 88 + "\033[0m")
    print()

    for line in difflib.unified_diff(
        orig_lines,
        new_lines,
        fromfile=str(path),
        tofile=str(path),
        lineterm="",
    ):
        # unified_diff gives lines without trailing newline because lineterm=""
        # so we add our own newline via plain print (no end argument).
        if line.startswith("+") and not line.startswith("+++"):
            print("\033[32m" + line + "\033[0m")  # green additions
        elif line.startswith("-") and not line.startswith("---"):
            print("\033[31m" + line + "\033[0m")  # red removals
        else:
            # context / header lines
            print(line)

    # Bottom separator + two blank lines between files
    print("\n" + "\033[36m" + "─" * 88 + "\033[0m" + "\n")

# ---------------------------------------------------------------------------
# File walking
# ---------------------------------------------------------------------------

def process_file(path: Path, spherescript_prefixes: List[str]) -> bool:
    """
    Read, process, and possibly overwrite a single .md file.

    Returns True if the file content changed, False otherwise.
    """
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Skipping (decode error): {path}")
        return False

    cleaned = process_markdown(original, spherescript_prefixes)

    if cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
        show_diff(original, cleaned, path)
        return True

    return False


def walk_and_process(root: Path) -> None:
    """Recursively process all .md files."""
    changed_files = []
    total = 0

    print(f"Processing Markdown files in: {root}")
    for p in root.rglob("*.md"):
        total += 1
        if process_file(p, DEFAULT_SPHERESCRIPT_PREFIXES):
            changed_files.append(p)

    print(f"\n{'='*70}")
    print(f"SUMMARY: Scanned {total} files, changed {len(changed_files)}")
    print(f"{'='*70}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 clean_markdown_wiki.py /path/to/root")
        sys.exit(1)

    root = Path(sys.argv[1]).expanduser().resolve()
    if not root.is_dir():
        print(f"Error: {root} is not a directory")
        sys.exit(1)

    print("SphereScript prefixes (case-insensitive): " + ", ".join(DEFAULT_SPHERESCRIPT_PREFIXES))

    walk_and_process(root)

if __name__ == "__main__":
    main()
