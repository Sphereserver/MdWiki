#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clean & normalize converted MediaWiki Markdown files (Production-Ready).

Key Features:
- Preserves internal whitespace/tabs (only trims trailing spaces).
- Converts HTML tables (<table>, <tr>, <td>, <th>, <tbody>) to aligned Markdown tables.
- Converts <ul>/<li> to Markdown bullet lists.
- Preserves valid Markdown tables, converts malformed ones.
- Shows colorized unified diff for changed files.
- Same-width column alignment in Markdown tables.

Usage:
    python3 clean_markdown_wiki.py /path/to/root
"""

import os
import re
import sys
import difflib
from pathlib import Path
from typing import List, Tuple
from collections import defaultdict

# MediaWiki magic words to remove (case-sensitive, exact match)
MEDIAWIKI_MAGIC_WORDS = [
    "__FORCETOC__", "__NOTOC__", "__TOC__", "__NOEDITSECTION__",
    "__NEWSECTIONLINK__", "__NONEWSECTIONLINK__", "__NOGALLERY__",
]

MAX_HEADER_WIDTH = 100


def remove_mediawiki_magic(text: str) -> str:
    """
    Remove MediaWiki magic words like __FORCETOC__.
    These are double-underscore wrapped directives that control TOC, editing, etc.
    """
    for word in MEDIAWIKI_MAGIC_WORDS:
        text = text.replace(word, "")
    return text

def convert_inline_html(text: str) -> str:
    """
    Convert ONLY actual HTML tags to Markdown. Preserves existing Markdown.

    1. <strong> and <b> -> **text**
       Regex: r"<\s*(strong|b)\b[^>]*>(.*?)</\s*(strong|b)\s*>"
       - \s* : optional whitespace
       - (strong|b)\b : captures 'strong' or 'b' as word boundary
       - [^>]* : any attributes until >
       - (.*?) : non-greedy capture of content
       - </\s*(strong|b)\s*> : matching closing tag

    2. <em> and <i> -> *text*

    3. <a href="URL">text</a> -> [text](URL)
       Regex: r'<\s*a\b[^>]*href\s*=\s*"([^"]*)"[^>]*>(.*?)</\s*a\s*>'
       - href\s*=\s*"([^"]*)" : captures URL in quotes (group 1)
       - (.*?) : captures link text (group 2)

    4. Remove layout <div>/<span> tags but keep content
    5. <p> -> paragraph breaks with blank lines
    """

    # <strong> and <b> -> **text** (only real HTML tags, not existing **bold**)
    def strong_replacer(m: re.Match) -> str:
        """Lambda: captures group 2 (content), wraps in ** **, strips whitespace."""
        return f"**{m.group(2).strip()}**"

    text = re.sub(
        r"<\s*(strong|b)\b[^>]*>(.*?)</\s*(strong|b)\s*>",
        strong_replacer,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # <em> and <i> -> *text*
    def em_replacer(m: re.Match) -> str:
        return f"*{m.group(2).strip()}*"

    text = re.sub(
        r"<\s*(em|i)\b[^>]*>(.*?)</\s*(em|i)\s*>",
        em_replacer,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # <a href="URL">text</a> -> [text](URL)
    def link_replacer(m: re.Match) -> str:
        """Lambda: group 1=URL, group 2=text. Use text or URL as fallback."""
        url = m.group(1).strip()
        label = m.group(2).strip()
        return f"[{label or url}]({url})"

    text = re.sub(
        r'<\s*a\b[^>]*href\s*=\s*"([^"]*)"[^>]*>(.*?)</\s*a\s*>',
        link_replacer,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Remove layout div/span but keep content (opening and closing separately)
    text = re.sub(r"<\s*(div|span)(\s+[^>]*)?>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</\s*(div|span)\s*>", "", text, flags=re.IGNORECASE)

    # <p> blocks -> paragraphs with blank line separation
    def p_replacer(m: re.Match) -> str:
        inner = m.group(1).strip()
        return f"\n\n{inner}\n\n" if inner else ""

    text = re.sub(r"<\s*p\b[^>]*>(.*?)</\s*p\s*>", p_replacer, text, flags=re.IGNORECASE | re.DOTALL)

    return text

def cleanup_cell_content(s: str) -> str:
    """
    Clean content inside table cells:
    - Remove structural tags: <tbody>, <tr>, <td>, <th>, </td>, </tr>
    - Apply inline HTML conversion
    - Normalize <br> tags to <br />
    """
    s = escape_md_special_chars(s)
    s = s.strip()

    # Remove ALL table structure tags: <tr>, </tr>, <td>, </td>, <th>, </th>, <tbody>
    # Regex: </?(tbody|tr|td|th)\b[^>]*> matches both opening <tag> and closing </tag>
    s = re.sub(r"</?tbody[^>]*>", "", s, flags=re.IGNORECASE)  # tbody tags
    s = re.sub(r"</?(tr|td|th)[^>]*>", "", s, flags=re.IGNORECASE)  # tr/td/th self-closing remnants

    # Apply inline HTML conversion to cell content
    s = convert_inline_html(s)

    # Normalize <br> tags
    s = re.sub(r"<\s*br\s*/?\s*>", "<br />", s, flags=re.IGNORECASE)

    return s.strip()

def escape_md_special_chars(text: str) -> str:
    """Escape Markdown special chars: * _ ` [ ] ( ) # + - > |"""
    special_chars = r'*_`\[\]()#+->|'
    return re.sub(re.escape(special_chars), lambda m: f'\\{m.group(0)}', text)

def convert_html_tables_to_markdown(text: str) -> str:
    """
    Convert HTML <table> blocks to aligned Markdown tables with same-width columns.

    Process:
    1. Find each <table>...</table> block
    2. Extract <tr> rows recursively (handles nested tables)
    3. Extract <th> or <td> cells from each row
    4. Calculate max width per column across all rows
    5. Pad cells with spaces to create aligned columns
    """

    def convert_single_table(m: re.Match) -> str:
        """Convert single <table>...</table> to Markdown table."""
        table_html = m.group(0)

        # Extract all <tr>...</tr> rows (recursive for nested tables)
        rows_html = re.findall(
            r"<\s*tr\b[^>]*>(.*?)</\s*tr\s*>",
            table_html,
            flags=re.IGNORECASE | re.DOTALL,
        )

        parsed_rows: List[List[str]] = []

        for row_html in rows_html:
            # Recursively convert nested tables first
            row_html = convert_html_tables_to_markdown(row_html)

            # First try <th> cells (headers), then <td> cells
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

            # Clean each cell and collect row
            cleaned_cells = [cleanup_cell_content(c) for c in cells]
            if cleaned_cells:
                parsed_rows.append(cleaned_cells)

        if not parsed_rows:
            return table_html  # No valid rows found, preserve original

        # Calculate column widths for alignment
        max_cols = max(len(row) for row in parsed_rows) or 1
        col_widths = [0] * max_cols

        for row in parsed_rows:
            for col_idx, cell in enumerate(row):
                if col_idx < max_cols:
                    col_widths[col_idx] = max(col_widths[col_idx], len(cell))

        # Build aligned Markdown table
        header = parsed_rows[0] + [""] * (max_cols - len(parsed_rows[0]))
        body_rows = [row + [""] * (max_cols - len(row)) for row in parsed_rows[1:]]

        md_lines = []

        # Header row (padded to column widths)
        header_line = "|"
        for i, cell in enumerate(header):
            padding = " " * (col_widths[i] - len(cell))
            header_line += f" {cell}{padding} |"
        md_lines.append(header_line)

        # Separator row (aligned dashes)
        sep_line = "|"
        for i, width in enumerate(col_widths):
            # Header uses min space needed for separator, capped at MAX_HEADER_WIDTH
            header_space = min(len(header[i]), MAX_HEADER_WIDTH)
            sep_line += f" {'-' * header_space} |"
        md_lines.append(sep_line)

        # Body rows (aligned)
        for row in body_rows:
            row_line = "|"
            for i, cell in enumerate(row):
                padding = " " * (col_widths[i] - len(cell))
                row_line += f" {cell}{padding} |"
            md_lines.append(row_line)

        return "\n".join(md_lines)

    # Replace ALL <table>...</table> blocks
    return re.sub(
        r"<\s*table\b[^>]*>.*?</\s*table\s*>",
        convert_single_table,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

def convert_html_lists_to_markdown(text: str) -> str:
    """
    Convert HTML <ul> and <li> to Markdown bullet lists.

    Regex patterns:
    - <ul>...</ul> : unordered list container
    - <li>...</li> : list items

    Process:
    1. Find each <ul>...</ul> block
    2. Extract all <li> items
    3. Convert to "- item" Markdown format
    """

    def convert_single_ul(m: re.Match) -> str:
        """Convert single <ul>...</ul> to Markdown bullet list."""
        ul_html = m.group(0)

        # Extract all <li>...</li> items
        li_items = re.findall(
            r"<\s*li\b[^>]*>(.*?)</\s*li\s*>",
            ul_html,
            flags=re.IGNORECASE | re.DOTALL,
        )

        if not li_items:
            return ul_html  # No items, preserve original

        # Clean each item and convert to Markdown bullet
        md_items = []
        for item in li_items:
            cleaned_item = convert_inline_html(item).strip()  # Apply inline cleanup
            if cleaned_item:
                md_items.append(f"- {cleaned_item}")

        return "\n".join(md_items)

    # Replace all <ul>...</ul> blocks with bullet lists
    return re.sub(
        r"<\s*ul\b[^>]*>.*?</\s*ul\s*>",
        convert_single_ul,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

def is_valid_md_table(lines: List[str]) -> bool:
    """
    Check if block is a valid Markdown table (preserve as-is).
    Requirements:
    - At least 2 lines (header + separator)
    - Header contains "|"
    - Separator contains "-" and "|"
    - Consistent column structure in first few rows
    """
    if len(lines) < 2:
        return False

    header = lines[0].strip()
    separator = lines[1].strip()

    if "|" not in header or ("-" not in separator and "|" not in separator):
        return False

    # Check first 3 rows have consistent pipes
    for line in lines[:3]:
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) == 0:
            return False

    return True

def normalize_md_tables(text: str) -> str:
    """
    ONLY normalize malformed Markdown tables. Valid tables preserved exactly.
    """
    lines = text.splitlines()
    out_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Potential table start: pipe + next line has dashes
        if "|" in line and i + 1 < len(lines) and "-" in lines[i + 1]:
            block_start = i
            # Collect entire table block
            while i < len(lines) and "|" in lines[i]:
                i += 1
            block_end = i

            block_lines = lines[block_start:block_end]

            # Skip normalization if table is already valid
            if is_valid_md_table(block_lines):
                out_lines.extend(block_lines)
            else:
                # Fix malformed table with aligned columns
                normalized_block = normalize_single_table_block(block_lines)
                out_lines.extend(normalized_block)
        else:
            out_lines.append(line)
            i += 1

    return "\n".join(out_lines)

def normalize_single_table_block(block_lines: List[str]) -> List[str]:
    """
    Fix malformed Markdown table with proper column alignment.
    1. Split rows into cells
    2. Calculate max width per column
    3. Pad cells for alignment
    """
    rows = []
    for line in block_lines:
        # Split by |, remove empty first/last, strip cells
        parts = [p.strip() for p in line.split("|")[1:-1]]
        rows.append(parts)

    if not rows:
        return block_lines

    max_cols = max(len(r) for r in rows) or 1
    col_widths = [0] * max_cols

    # Calculate column widths
    for row in rows:
        for col_idx, cell in enumerate(row):
            if col_idx < max_cols:
                col_widths[col_idx] = max(col_widths[col_idx], len(cell))

    # Build aligned table
    header = rows[0] + [""] * (max_cols - len(rows[0]))
    normalized = []

    # Header row
    header_line = "|"
    for i, cell in enumerate(header):
        padding = " " * (col_widths[i] - len(cell))
        header_line += f" {cell}{padding} |"
    normalized.append(header_line)

    # Separator row
    sep_line = "|"
    for i, width in enumerate(col_widths):
        header_space = min(len(header[i]), MAX_HEADER_WIDTH)
        sep_line += f" {'-' * header_space} |"

    # Body rows
    for row in rows[1:]:
        row_line = "|"
        padded_row = row + [""] * (max_cols - len(row))
        for i, cell in enumerate(padded_row):
            padding = " " * (col_widths[i] - len(cell))
            row_line += f" {cell}{padding} |"
        normalized.append(row_line)

    return normalized

def normalize_spacing_safely(text: str) -> str:
    """
    ONLY trim trailing whitespace. Preserve:
    - Leading spaces/tabs
    - Internal spaces/tabs
    - Multiple spaces between words
    """
    lines = []
    for line in text.splitlines():
        # rstrip() removes ONLY trailing whitespace
        lines.append(line.rstrip())

    result = "\n".join(lines)
    # Ensure single trailing newline
    if result and not result.endswith("\n"):
        result += "\n"

    return result

def process_markdown(text: str) -> str:
    """Main processing pipeline (order matters!)."""
    # 1. Remove MediaWiki magic words FIRST
    text = remove_mediawiki_magic(text)

    # 2. HTML lists (<ul>/<li>)
    text = convert_html_lists_to_markdown(text)

    # 3. HTML tables (<table>/<tr>/<td>/<th>/<tbody>)
    text = convert_html_tables_to_markdown(text)

    # 4. Inline HTML (<strong>, <em>, <a>, <p>, <div>)
    text = convert_inline_html(text)

    # 5. Normalize malformed Markdown tables only
    text = normalize_md_tables(text)

    # 6. Safe spacing normalization (trailing whitespace only)
    text = normalize_spacing_safely(text)

    return text

def show_diff(original: str, cleaned: str, path: Path) -> None:
    """Display colorized unified diff."""
    orig_lines = original.splitlines(keepends=True)
    new_lines = cleaned.splitlines(keepends=True)

    print(f"\n{'='*70}")
    print(f"CHANGED: {path}")
    print(f"{'='*70}")

    for line in difflib.unified_diff(
        orig_lines, new_lines,
        fromfile=str(path),
        tofile=str(path),
        lineterm=""
    ):
        if line.startswith("+") and not line.startswith("+++"):
            print(f"\033[32m{line}\033[0m", end="")  # Green additions
        elif line.startswith("-") and not line.startswith("---"):
            print(f"\033[31m{line}\033[0m", end="")  # Red removals
        else:
            print(line, end="")
    print()

def process_file(path: Path) -> bool:
    """Process single .md file, show diff if changed."""
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Skipping (decode error): {path}")
        return False

    cleaned = process_markdown(original)

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
        if process_file(p):
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

    walk_and_process(root)

if __name__ == "__main__":
    main()
