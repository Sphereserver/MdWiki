#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clean & normalize converted MediaWiki Markdown files.

- Recursively process .md files from a given root directory.
- Remove MediaWiki magic words like __FORCETOC__.
- Preserve custom tags like <font> and <spherescript>.
- Convert common HTML tags (strong, em, p, a) to Markdown.
- Convert simple HTML tables (including nested ones) to Markdown tables.
- Validate and normalize Markdown table formatting.
- Normalize trailing spaces and blank lines.
- Report which files were changed.

Usage:
    python3 clean_markdown_wiki.py /path/to/root
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

# ---------------------------------------------------------------------------
# MediaWiki-specific cleanup
# ---------------------------------------------------------------------------

MEDIAWIKI_MAGIC_WORDS = [
    "__FORCETOC__",
    "__NOTOC__",
    "__TOC__",
    "__NOEDITSECTION__",
    "__NEWSECTIONLINK__",
    "__NONEWSECTIONLINK__",
    "__NOGALLERY__",
]

def remove_mediawiki_magic(text: str) -> str:
    """Remove common MediaWiki magic words like __FORCETOC__."""
    for word in MEDIAWIKI_MAGIC_WORDS:
        text = text.replace(word, "")
    return text


# ---------------------------------------------------------------------------
# HTML to Markdown conversions (inline)
# ---------------------------------------------------------------------------

def convert_inline_html(text: str) -> str:
    """
    Convert common inline HTML tags to Markdown equivalents.
    - <strong>, <b> -> **
    - <em>, <i>     -> *
    - <a href="..">text</a> -> [text](url)
    - <p>...</p> -> blank line separated paragraphs
    - <div>, <span> -> remove tag, keep content
    Custom tags like <font>, <spherescript> are preserved.
    """

    # <strong> and <b> -> **...**
    text = re.sub(
        r"<\s*(strong|b)\s*>(.*?)<\s*/\s*\1\s*>",
        lambda m: f"**{m.group(2).strip()}**",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # <em> and <i> -> *...*
    text = re.sub(
        r"<\s*(em|i)\s*>(.*?)<\s*/\s*\1\s*>",
        lambda m: f"*{m.group(2).strip()}*",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # <a href="url">text</a> -> [text](url)
    def _replace_link(m: re.Match) -> str:
        url = m.group(1).strip()
        label = m.group(2).strip()
        if not label:
            label = url
        return f"[{label}]({url})"

    text = re.sub(
        r'<\s*a\s+[^>]*href\s*=\s*"(.*?)"[^>]*>(.*?)<\s*/\s*a\s*>',
        _replace_link,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # <p>...</p> -> blank-line separated paragraphs
    def _replace_p(m: re.Match) -> str:
        inner = m.group(1).strip()
        if not inner:
            return ""
        return "\n\n" + inner + "\n\n"

    text = re.sub(
        r"<\s*p\s*>(.*?)<\s*/\s*p\s*>",
        _replace_p,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Remove <div> and <span> tags but keep content
    text = re.sub(
        r"<\s*(div|span)(\s+[^>]*)?>",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"<\s*/\s*(div|span)\s*>",
        "",
        text,
        flags=re.IGNORECASE,
    )

    # NOTE:
    # - <font> and <spherescript> intentionally left as-is.
    # - Table tags handled separately.

    return text


# ---------------------------------------------------------------------------
# HTML table to Markdown table
# ---------------------------------------------------------------------------

def cleanup_cell_content(s: str) -> str:
    """
    Clean content inside table cells:
    - Run inline HTML conversion (strong/em/a).
    - Normalize <br> to <br /> (so it remains as explicit line breaks).
    - Strip residual tags like <tbody>, <tr>, <td>, <p> around the text.
    """
    s = s.strip()

    # Remove block-level tags wrapping a cell
    s = re.sub(r"</?(tbody|tr|td|th)\b[^>]*>", "", s, flags=re.IGNORECASE)
    s = re.sub(r"<\s*p\s*>", "", s, flags=re.IGNORECASE)
    s = re.sub(r"<\s*/\s*p\s*>", "", s, flags=re.IGNORECASE)

    # Inline conversions
    s = convert_inline_html(s)

    # Normalize <br>
    s = re.sub(r"<\s*br\s*/?\s*>", "<br />", s, flags=re.IGNORECASE)

    return s.strip()


def convert_html_tables_to_markdown(text: str) -> str:
    """
    Convert HTML <table> blocks into Markdown tables.

    - Handles simple tables and nested tables in a nested way:
      each HTML <table> becomes a standalone Markdown table.
    - If a table is too weird (e.g. no <tr>), it's left as-is.
    """

    def _convert_single_table(m: re.Match) -> str:
        table_html = m.group(0)

        # Extract rows
        rows_html = re.findall(
            r"<\s*tr\b[^>]*>(.*?)<\s*/\s*tr\s*>",
            table_html,
            flags=re.IGNORECASE | re.DOTALL,
        )
        parsed_rows: List[List[str]] = []

        for row_html in rows_html:
            # Nested tables inside cells: convert them first recursively
            row_html = convert_html_tables_to_markdown(row_html)

            # First look for header cells
            cells = re.findall(
                r"<\s*th\b[^>]*>(.*?)<\s*/\s*th\s*>",
                row_html,
                flags=re.IGNORECASE | re.DOTALL,
            )
            is_header_row = True
            if not cells:
                # Fallback to data cells
                cells = re.findall(
                    r"<\s*td\b[^>]*>(.*?)<\s*/\s*td\s*>",
                    row_html,
                    flags=re.IGNORECASE | re.DOTALL,
                )
                is_header_row = False

            cleaned_cells = [cleanup_cell_content(c) for c in cells]
            if cleaned_cells:
                parsed_rows.append((cleaned_cells, is_header_row))

        if not parsed_rows:
            return table_html  # give up, keep original

        # Determine column count
        max_cols = max(len(r[0]) for r in parsed_rows)
        if max_cols == 0:
            return table_html

        # Build normalized rows (pad to max_cols)
        header_cells = None
        body_rows: List[List[str]] = []

        # Prefer first header row as Markdown header; if none, use first row
        header_index = None
        for idx, (cells, is_header) in enumerate(parsed_rows):
            if is_header:
                header_index = idx
                break
        if header_index is None:
            header_index = 0

        for idx, (cells, _) in enumerate(parsed_rows):
            padded = cells + [""] * (max_cols - len(cells))
            if idx == header_index:
                header_cells = padded
            else:
                body_rows.append(padded)

        if header_cells is None:
            return table_html  # shouldn't happen, but safe

        md_lines: List[str] = []
        md_lines.append("| " + " | ".join(header_cells) + " |")
        md_lines.append("| " + " | ".join(["---"] * max_cols) + " |")
        for row in body_rows:
            md_lines.append("| " + " | ".join(row) + " |")

        return "\n".join(md_lines)

    # Replace each <table>...</table> block with a Markdown table
    return re.sub(
        r"<\s*table\b[^>]*>.*?<\s*/\s*table\s*>",
        _convert_single_table,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )


# ---------------------------------------------------------------------------
# Markdown table normalization/linting
# ---------------------------------------------------------------------------

def normalize_md_tables(text: str) -> str:
    """
    Detect Markdown tables and normalize them:
    - Consistent column counts.
    - Standard header/separator form.
    - Normalize spacing inside cells.
    """

    lines = text.splitlines()
    out_lines: List[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # Heuristic: table header candidate
        if "|" in line and not line.strip().startswith(("#", "-", "*")):
            if i + 1 < n and is_separator_line(lines[i + 1]):
                # Collect contiguous table lines
                block = [line]
                j = i + 1
                while j < n and "|" in lines[j]:
                    block.append(lines[j])
                    j += 1
                normalized_block = normalize_single_table_block(block)
                out_lines.extend(normalized_block)
                i = j
                continue

        out_lines.append(line)
        i += 1

    return "\n".join(out_lines)


def is_separator_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    # Must have '-' and '|'
    return "-" in stripped and "|" in stripped


def split_md_row(row: str) -> List[str]:
    row = row.strip()
    if not row.startswith("|"):
        row = "| " + row
    if not row.endswith("|"):
        row = row + " |"

    parts = row.split("|")
    parts = parts[1:-1]
    parts = [p.strip() for p in parts]
    return parts


def normalize_single_table_block(block_lines: List[str]) -> List[str]:
    """
    Normalize one contiguous block of Markdown table lines:
    - Fix header and separator.
    - Ensure every row has same number of columns.
    """

    if not block_lines:
        return []

    rows = [split_md_row(l) for l in block_lines]
    max_cols = max(len(r) for r in rows)
    if max_cols == 0:
        return block_lines

    padded_rows = [r + [""] * (max_cols - len(r)) for r in rows]

    header = padded_rows[0]

    # If second row looks like separator, skip its content and rebuild
    if len(padded_rows) > 1 and all(set(c) <= {"", "-", ":"} for c in padded_rows[1]):
        body = padded_rows[2:]
    else:
        body = padded_rows[1:]

    sep = ["---"] * max_cols

    normalized = []
    normalized.append("| " + " | ".join(header) + " |")
    normalized.append("| " + " | ".join(sep) + " |")
    for r in body:
        normalized.append("| " + " | ".join(r) + " |")

    return normalized


# ---------------------------------------------------------------------------
# General whitespace normalization
# ---------------------------------------------------------------------------

def normalize_spacing(text: str) -> str:
    """
    - Strip trailing spaces on each line.
    - Collapse more than 2 consecutive blank lines into max 2.
    """
    lines = [line.rstrip() for line in text.splitlines()]

    normalized: List[str] = []
    blank_count = 0
    for line in lines:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= 2:
                normalized.append("")
        else:
            blank_count = 0
            normalized.append(line)

    return "\n".join(normalized)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def process_markdown(text: str) -> str:
    """Apply all cleanup steps to a single Markdown document."""
    # 1. Remove MediaWiki magic words
    text = remove_mediawiki_magic(text)

    # 2. HTML tables -> Markdown tables (before inline conversion so we can treat cell content)
    text = convert_html_tables_to_markdown(text)

    # 3. Convert inline HTML (strong/em/a/p/div/span)
    text = convert_inline_html(text)

    # 4. Normalize Markdown tables
    text = normalize_md_tables(text)

    # 5. Normalize spacing
    text = normalize_spacing(text)

    return text


def process_file(path: Path) -> bool:
    """Process a single .md file. Return True if file changed."""
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Skipping (decode error): {path}")
        return False

    cleaned = process_markdown(original)

    if cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
        return True
    return False


def walk_and_process(root: Path) -> None:
    changed_files: List[Path] = []
    total = 0
    for p in root.rglob("*.md"):
        total += 1
        if process_file(p):
            changed_files.append(p)

    print(f"Scanned {total} markdown files.")
    print(f"Changed {len(changed_files)} file(s):")
    for p in changed_files:
        try:
            print("  -", p.relative_to(root))
        except ValueError:
            print("  -", p)


def main():
    if len(sys.argv) != 2:
        print("Usage: clean_markdown_wiki.py /path/to/root_folder")
        raise SystemExit(1)

    root = Path(sys.argv[1]).expanduser().resolve()
    if not root.is_dir():
        print(f"Not a directory: {root}")
        raise SystemExit(1)

    walk_and_process(root)


if __name__ == "__main__":
    main()
