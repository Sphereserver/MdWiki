#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clean & normalize converted MediaWiki Markdown files (Sphere-ready).

Main features:
- Recursively process .md files in a tree.
- Remove MediaWiki magic words like __FORCETOC__.
- Convert HTML tables (<table>, <tr>, <td>, <th>, <tbody>) to Markdown tables.
- Convert <ul>/<li> to Markdown bullet lists.
- Convert inline HTML (<strong>, <em>, <a>, <div>, <span>) to Markdown or strip layout tags.
- Normalize / repair malformed Markdown tables.
- Preserve internal whitespace; trim only trailing spaces.
- SphereScript handling:
  - Inline highlighting: prefixes (TAG., T_, DEF., etc.), control-flow keywords, [BLOCK]-style markers.
  - Code block fencing: detect SphereScript syntax and wrap contiguous regions in ```
- Unwrap hard-wrapped paragraphs (common in MediaWiki exports).
- Colorized unified diff with clear separators and spacing.

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
# ANSI color constants
# ---------------------------------------------------------------------------
CYAN = "\x1b[36m"
GREEN = "\x1b[32m"
RED = "\x1b[31m"
RESET = "\x1b[0m"

# ---------------------------------------------------------------------------
# Global constants
# ---------------------------------------------------------------------------

# Maximum total width for deciding when to use compact table separators
MAX_TABLE_WIDTH = 120

# Minimum separator width (number of dashes)
MIN_SEPARATOR_WIDTH = 3

# Default SphereScript prefixes for highlighting (case-insensitive).
# NOTE: "RETURN" removed to avoid backticking prose like "Return Values"
DEFAULT_SPHERESCRIPT_PREFIXES = [
    "TAG.", "TAG0.", "T_", "DEF.", "DEF0.", "DEFMSG.", "DEFMSG0.",
    "CTAG.", "CTAG0.", "VAR.", "VAR0.", "LIST.", "SERV.", "I.",
    "SRC.", "NEW.", "ON=",
]

# MediaWiki magic words to remove (case-sensitive, exact match)
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
        help="SphereScript identifier prefixes to highlight with backticks.",
    )
    return parser.parse_args()

# ---------------------------------------------------------------------------
# Generic helpers
# ---------------------------------------------------------------------------

def remove_mediawiki_magic(text: str) -> str:
    """Remove MediaWiki magic words like __FORCETOC__ from the text."""
    for word in MEDIAWIKI_MAGIC_WORDS:
        text = text.replace(word, "")
        escaped = word.replace("_", r"\_")
        text = text.replace(escaped, "")
    return text

def remove_spherescript_tags(text: str) -> str:
    """Remove <spherescript>...</spherescript> tags but keep their inner content."""
    return re.sub(
        r"<\s*spherescript\b[^>]*>(.*?)</\s*spherescript\s*>",
        lambda m: m.group(1),
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

def fix_broken_links(text: str) -> str:
    """Fix links broken by newlines, e.g. [map\npoints] -> [map points]."""
    text = re.sub(
        r"\[([^\]]*?)\n([^\]]*?)\]",
        lambda m: f"[{m.group(1).strip()} {m.group(2).strip()}]",
        text,
    )
    text = re.sub(
        r"\(([^)]*?)\n([^)]*?)\)",
        lambda m: f"({m.group(1).strip()}{m.group(2).strip()})",
        text,
    )
    return text

def normalize_spacing_safely(text: str) -> str:
    """Trim trailing whitespace and collapse excessive blank lines (max 2)."""
    lines = [line.rstrip() for line in text.splitlines()]

    # Collapse excessive blank lines
    result_lines = []
    blank_count = 0
    for line in lines:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= 2:
                result_lines.append(line)
        else:
            blank_count = 0
            result_lines.append(line)

    result = "\n".join(result_lines)
    if result and not result.endswith("\n"):
        result += "\n"
    return result

# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------

def line_is_table_row(line: str) -> bool:
    """Check if a line looks like a Markdown table row."""
    stripped = line.lstrip()
    return stripped.startswith("|") and stripped.count("|") >= 2

def line_is_header(line: str) -> bool:
    """Check if a line is a Markdown header (starts with #)."""
    return line.lstrip().startswith("#")

# ---------------------------------------------------------------------------
# Inline HTML → Markdown
# ---------------------------------------------------------------------------

def convert_inline_html(text: str) -> str:
    """Convert common inline HTML tags to Markdown equivalents."""
    # <strong> / <b> → **...**
    text = re.sub(
        r"<\s*(strong|b)\b[^>]*>(.*?)</\s*(strong|b)\s*>",
        lambda m: f"**{m.group(2).strip()}**" if m.group(2).strip() else "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    # <em> / <i> → *...*
    text = re.sub(
        r"<\s*(em|i)\b[^>]*>(.*?)</\s*(em|i)\s*>",
        lambda m: f"*{m.group(2).strip()}*" if m.group(2).strip() else "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    # <a href="url">text</a> → [text](url)
    text = re.sub(
        r'<\s*a\b[^>]*href\s*=\s*"([^"]*)"[^>]*>(.*?)</\s*a\s*>',
        lambda m: f"[{m.group(2).strip() or m.group(1).strip()}]({m.group(1).strip()})",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    # Strip <div>/<span>
    text = re.sub(r"<\s*(div|span)\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</\s*(div|span)\s*>", "", text, flags=re.IGNORECASE)
    return text

# ---------------------------------------------------------------------------
# HTML tables → Markdown tables
# ---------------------------------------------------------------------------

def sanitize_cell_text(s: str) -> str:
    """Sanitize cell text: convert non-breaking spaces, collapse multiple spaces."""
    s = s.replace('\xa0', ' ')
    s = re.sub(r'\s{2,}', ' ', s)
    return s.strip()

def cleanup_cell_content(s: str) -> str:
    """Clean content inside table cells."""
    s = s.strip()
    # <code> → backticks
    s = re.sub(
        r"<\s*code\b[^>]*>(.*?)</\s*code\s*>",
        lambda m: f"`{m.group(1).strip()}`" if m.group(1).strip() else "",
        s,
        flags=re.IGNORECASE | re.DOTALL,
    )
    # Newlines and <br> → spaces
    s = s.replace("\n", " ")
    s = re.sub(r"<\s*br\s*/?\s*>", " ", s, flags=re.IGNORECASE)
    # Remove table-structure tags
    s = re.sub(r"</?tbody[^>]*>", "", s, flags=re.IGNORECASE)
    s = re.sub(r"</?(tr|td|th)\b[^>]*>", "", s, flags=re.IGNORECASE)
    # Flatten lists
    s = re.sub(
        r"<\s*li\b[^>]*>(.*?)</\s*li\s*>",
        lambda m: f"{m.group(1).strip()}; " if m.group(1).strip() else "",
        s,
        flags=re.IGNORECASE | re.DOTALL,
    )
    s = re.sub(r"</?(ul|ol)\b[^>]*>", "", s, flags=re.IGNORECASE)
    # Remove <p> wrappers
    s = re.sub(
        r"<\s*p\b[^>]*>(.*?)</\s*p\s*>",
        lambda m: m.group(1).strip(),
        s,
        flags=re.IGNORECASE | re.DOTALL,
    )
    # Inline HTML
    s = convert_inline_html(s)
    # Final cleanup
    s = sanitize_cell_text(s)
    s = re.sub(r";\s*;", ";", s)
    s = s.strip(" ;")
    # Escape pipes
    s = s.replace("|", r"\|")
    return s.strip()

def convert_html_tables_to_markdown(text: str) -> str:
    """Convert all HTML <table>...</table> blocks to Markdown tables."""

    def convert_single_table(m: Match) -> str:
        table_html = m.group(0)

        rows_html = re.findall(
            r"<\s*tr\b[^>]*>(.*?)</\s*tr\s*>",
            table_html,
            flags=re.IGNORECASE | re.DOTALL,
        )

        parsed_rows: List[List[str]] = []
        for row_html in rows_html:
            row_html = convert_html_tables_to_markdown(row_html)
            th_cells = re.findall(
                r"<\s*th\b[^>]*>(.*?)</\s*th\s*>",
                row_html,
                flags=re.IGNORECASE | re.DOTALL,
            )
            cells = th_cells if th_cells else re.findall(
                r"<\s*td\b[^>]*>(.*?)</\s*td\s*>",
                row_html,
                flags=re.IGNORECASE | re.DOTALL,
            )
            cleaned_cells = [cleanup_cell_content(c) for c in cells]
            if cleaned_cells:
                parsed_rows.append(cleaned_cells)

        if not parsed_rows:
            return table_html

        max_cols = max(len(row) for row in parsed_rows) if parsed_rows else 1

        # Pad all rows
        for row in parsed_rows:
            while len(row) < max_cols:
                row.append("")

        # Check if any cell is long (use compact separator if so)
        max_cell_len = max((len(cell) for row in parsed_rows for cell in row), default=0)
        use_compact = max_cell_len > 60

        md_lines: List[str] = []

        # FIXED: Use first row as header, not the entire parsed_rows list
        header_row = parsed_rows[0]
        header_line = "| " + " | ".join(header_row) + " |"
        md_lines.append(header_line)

        # Separator
        if use_compact:
            sep_line = "| " + " | ".join(["-" * MIN_SEPARATOR_WIDTH] * max_cols) + " |"
        else:
            col_widths = [max(len(row[i]) for row in parsed_rows) for i in range(max_cols)]
            col_widths = [max(w, MIN_SEPARATOR_WIDTH) for w in col_widths]
            sep_line = "| " + " | ".join(["-" * w for w in col_widths]) + " |"
        md_lines.append(sep_line)

        # Body rows
        for row in parsed_rows[1:]:
            row_line = "| " + " | ".join(row) + " |"
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
    """Convert <ul>...</ul> + <li>...</li> into Markdown bullet lists."""

    def convert_single_ul(m: Match) -> str:
        ul_html = m.group(0)
        li_items = re.findall(
            r"<\s*li\b[^>]*>(.*?)</\s*li\s*>",
            ul_html,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if not li_items:
            return ul_html
        md_items = []
        for item in li_items:
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
# Markdown table normalization
# ---------------------------------------------------------------------------

def is_valid_md_table(lines: List[str]) -> bool:
    """Check whether a block of lines is already a valid Markdown table."""
    if len(lines) < 2:
        return False
    header = lines[0].strip()
    separator = lines[1].strip()
    if "|" not in header or "-" not in separator or "|" not in separator:
        return False
    return True

def normalize_single_table_block(block_lines: List[str]) -> List[str]:
    """Fix a malformed Markdown table."""
    rows: List[List[str]] = []
    for line in block_lines:
        s = line.strip()
        if s.startswith("|"):
            s = s[1:]
        if s.endswith("|"):
            s = s[:-1]
        parts = s.split("|")
        rows.append([sanitize_cell_text(p) for p in parts])

    if not rows:
        return block_lines

    # Filter out separator rows for column calculation
    data_rows = [r for i, r in enumerate(rows) if i != 1 or not all(c.replace('-', '').strip() == '' for c in r)]

    max_cols = max(len(r) for r in data_rows) if data_rows else 1

    # Pad rows
    for row in data_rows:
        while len(row) < max_cols:
            row.append("")

    # Check for compact separator
    max_cell_len = max((len(cell) for row in data_rows for cell in row), default=0)
    use_compact = max_cell_len > 60

    normalized: List[str] = []

    # FIXED: Use first data row as header
    header_row = data_rows[0] if data_rows else [""] * max_cols
    header_line = "| " + " | ".join(header_row) + " |"
    normalized.append(header_line)

    # Separator
    if use_compact:
        sep_line = "| " + " | ".join(["-" * MIN_SEPARATOR_WIDTH] * max_cols) + " |"
    else:
        col_widths = [max(len(row[i]) if i < len(row) else 0 for row in data_rows) for i in range(max_cols)]
        col_widths = [max(w, MIN_SEPARATOR_WIDTH) for w in col_widths]
        sep_line = "| " + " | ".join(["-" * w for w in col_widths]) + " |"
    normalized.append(sep_line)

    # Body rows
    for row in data_rows[1:]:
        row_line = "| " + " | ".join(row) + " |"
        normalized.append(row_line)

    return normalized

def normalize_md_tables(text: str) -> str:
    """Scan for Markdown tables and normalize only the malformed ones."""
    lines = text.splitlines()
    out_lines: List[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        if "|" in line and i + 1 < n and "-" in lines[i + 1] and "|" in lines[i + 1]:
            block_start = i
            while i < n and "|" in lines[i]:
                i += 1
            block_lines = lines[block_start:i]
            if is_valid_md_table(block_lines):
                out_lines.extend(block_lines)
            else:
                out_lines.extend(normalize_single_table_block(block_lines))
        else:
            out_lines.append(line)
            i += 1

    return "\n".join(out_lines)

# ---------------------------------------------------------------------------
# SphereScript highlighting
# ---------------------------------------------------------------------------

def highlight_spherescript(text: str, prefixes: List[str]) -> str:
    """Highlight SphereScript constructs using backticks."""
    prefixes_pattern = "|".join(re.escape(p.lower()) for p in prefixes)
    cf_pattern = r"^\s*(IF|ELSEIF|ELSE|ENDIF|WHILE|ENDWHILE|FOR\w*|ENDFOR|DOSWITCH|ENDDO)\b"

    lines = text.splitlines()
    out_lines: List[str] = []
    in_fence = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue

        if in_fence or line_is_table_row(line) or line_is_header(line):
            out_lines.append(line)
            continue

        # Prefix-based identifiers
        line = re.sub(
            rf"\b({prefixes_pattern})[A-Za-z0-9_.]*",
            lambda m: f"`{m.group(0)}`",
            line,
            flags=re.IGNORECASE,
        )

        # Control-flow keywords
        line = re.sub(
            cf_pattern,
            lambda m: m.group(0).replace(m.group(1), f"`{m.group(1)}`", 1),
            line,
            flags=re.IGNORECASE,
        )

        # Bracket block at start - but NOT if followed by ( (which is a link)
        line = re.sub(
            r"^\s*(\[[^\]\n]+\])(?!\s*\()",
            lambda m: f"`{m.group(1)}`",
            line,
        )

        # RETURN only when followed by number/operator
        line = re.sub(
            r"\bRETURN\s*([0-9]|[=<>!]|$)",
            lambda m: f"`RETURN`{m.group(1)}",
            line,
            flags=re.IGNORECASE,
        )

        out_lines.append(line)

    return "\n".join(out_lines)

# ---------------------------------------------------------------------------
# SphereScript code block fencing
# ---------------------------------------------------------------------------

def fence_spherescript_blocks(text: str, prefixes: List[str]) -> str:
    """Detect likely SphereScript lines and wrap contiguous runs in ``` fences."""
    cf_start_re = re.compile(r"^\s*(IF|WHILE|FOR\w*|DOSWITCH)\b", re.IGNORECASE)
    cf_end_re = re.compile(r"^\s*(ENDIF|ENDWHILE|ENDFOR|ENDDO)\b", re.IGNORECASE)

    lines = text.splitlines()
    result: List[str] = []

    in_block = False
    in_md_fence = False
    in_comment_block = False
    cf_level = 0

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_block:
                result.append("```")
                in_block = False
            in_md_fence = not in_md_fence
            result.append(line)
            continue

        if in_md_fence:
            result.append(line)
            continue

        if line_is_table_row(line) or line_is_header(line):
            if in_block:
                result.append("```")
                in_block = False
            result.append(line)
            continue

        is_code = False

        # Multi-line comments
        if not in_comment_block and "/*" in stripped and "*/" not in stripped:
            in_comment_block = True
            is_code = True
        elif in_comment_block:
            is_code = True
            if "*/" in stripped:
                in_comment_block = False

        if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*/"):
            is_code = True

        if cf_start_re.match(stripped):
            cf_level += 1
            is_code = True
        elif cf_end_re.match(stripped):
            is_code = True
            cf_level = max(cf_level - 1, 0)
        elif cf_level > 0:
            is_code = True

        if not is_code and stripped.startswith("@") and not re.match(r"^\[@[^\]]+\]\(", stripped):
            is_code = True

        if not is_code and re.match(r"^\s*[\w\.\[\]]+\s*=", stripped) and not stripped.startswith("- ") and len(stripped.split()) <= 4:
            is_code = True

        if is_code and not in_block:
            result.append("```")
            in_block = True
        elif not is_code and in_block:
            result.append("```")
            in_block = False

        result.append(line)

    if in_block:
        result.append("```")

    return "\n".join(result)

# ---------------------------------------------------------------------------
# Remove <code> html tag (outside tables)
# ---------------------------------------------------------------------------

def convert_inline_code_outside_tables(text: str) -> str:
    """Simple global <code> → `...` for non-table content."""
    return re.sub(
        r"<\s*code\b[^>]*>(.*?)</\s*code\s*>",
        lambda m: f"`{m.group(1).strip()}`" if m.group(1).strip() else "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

# ---------------------------------------------------------------------------
# Unwrap hard-wrapped paragraphs
# ---------------------------------------------------------------------------

def unwrap_hard_wrapped_paragraphs(text: str) -> str:
    """
    Remove hard line wraps within paragraphs (common in MediaWiki exports).

    Joins consecutive lines that are part of the same paragraph, while preserving:
    - Blank lines (paragraph breaks)
    - List items (-, *, 1., etc.)
    - Headers (##)
    - Code blocks (```)
    - Table rows (|)
    """
    lines = text.splitlines()
    result: List[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # Preserve these lines as-is
        if (not stripped or 
            line_is_header(line) or
            stripped.startswith("```") or
            line_is_table_row(line) or
            re.match(r"^\s*[-*+]\s", line) or
            re.match(r"^\s*\d+\.\s", line) or
            line.endswith("  ")):
            result.append(line)
            i += 1
            continue

        # Collect paragraph lines
        paragraph_lines = [line]
        i += 1

        while i < n:
            next_line = lines[i]
            next_stripped = next_line.strip()

            # Stop at special lines
            if (not next_stripped or
                line_is_header(next_line) or
                next_stripped.startswith("```") or
                line_is_table_row(next_line) or
                re.match(r"^\s*[-*+]\s", next_line) or
                re.match(r"^\s*\d+\.\s", next_line)):
                break

            paragraph_lines.append(next_line)
            i += 1

        # Join with space
        indent = line[:len(line) - len(line.lstrip())]
        joined = " ".join(l.strip() for l in paragraph_lines)
        result.append(indent + joined)

    return "\n".join(result)

# ---------------------------------------------------------------------------
# Main processing pipeline
# ---------------------------------------------------------------------------

def process_markdown(text: str, spherescript_prefixes: List[str]) -> str:
    """Apply all cleanup and normalization steps to a single Markdown document."""
    text = remove_mediawiki_magic(text)
    text = remove_spherescript_tags(text)
    text = convert_html_tables_to_markdown(text)
    text = convert_html_lists_to_markdown(text)
    text = convert_inline_code_outside_tables(text)
    text = convert_inline_html(text)
    text = fix_broken_links(text)
    text = normalize_md_tables(text)
    text = fence_spherescript_blocks(text, spherescript_prefixes)
    text = highlight_spherescript(text, spherescript_prefixes)
    text = unwrap_hard_wrapped_paragraphs(text)
    text = normalize_spacing_safely(text)
    return text

# ---------------------------------------------------------------------------
# Diff output
# ---------------------------------------------------------------------------

def show_diff(original: str, cleaned: str, path: Path) -> None:
    """Print a colorized unified diff for a file."""
    orig_lines = original.splitlines(keepends=True)
    new_lines = cleaned.splitlines(keepends=True)

    print()
    print(CYAN + "═" * 88 + RESET)
    print(CYAN + f"File: {path}" + RESET)
    print(CYAN + "═" * 88 + RESET)
    print()

    for line in difflib.unified_diff(orig_lines, new_lines, fromfile=str(path), tofile=str(path), lineterm=""):
        if line.startswith("+") and not line.startswith("+++"):
            print(GREEN + line + RESET)
        elif line.startswith("-") and not line.startswith("---"):
            print(RED + line + RESET)
        else:
            print(line)

    print()
    print()

# ---------------------------------------------------------------------------
# File walking
# ---------------------------------------------------------------------------

def process_file(path: Path, spherescript_prefixes: List[str]) -> bool:
    """Read, process, and possibly overwrite a single .md file."""
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

def main() -> None:
    """Entry point: walk directory tree and process all .md files."""
    args = parse_arguments()
    root = Path(args.root).expanduser().resolve()

    if not root.is_dir():
        print(f"Error: {root} is not a directory")
        sys.exit(1)

    spherescript_prefixes = args.spherescript_prefixes
    changed_files: List[Path] = []
    total = 0

    print(f"Processing Markdown files in: {root}")
    print("SphereScript prefixes (case-insensitive): " + ", ".join(spherescript_prefixes))

    for p in root.rglob("*.md"):
        total += 1
        if process_file(p, spherescript_prefixes):
            changed_files.append(p)

    print(CYAN + "═" * 88 + RESET)
    print(f"SUMMARY: Scanned {total} files, changed {len(changed_files)}")
    print(CYAN + "═" * 88 + RESET)

if __name__ == "__main__":
    main()
