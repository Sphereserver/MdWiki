#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clean & normalize converted MediaWiki Markdown files (Sphere-ready).

Main features:
- Recursively process .md files in a tree.
- Remove MediaWiki magic words like __FORCETOC__.
- Convert HTML tables (<table>...) to Markdown tables.
- Convert HTML lists (<ul>/<li>) to Markdown lists.
- Convert inline HTML: <strong>, <em>, <code>, <a href=...>.
- Normalize malformed Markdown tables (alignment, cell padding).
- Fence detected SphereScript code blocks in ```.
- Highlight SphereScript identifiers (TAG., DEF., etc.) with backticks.
- Fix links broken by line wrapping.

Usage:
    python3 clean_markdown_wiki.py /path/to/root
    python3 clean_markdown_wiki.py /path --spherescript-prefixes TAG. T_ DEF. DEF0.

Changes are written back to each file in-place.
A colorized diff is printed on stdout for every file that changed.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path
from typing import List, Match

# ---------------------------------------------------------------------------
# ANSI escape codes for colored diffs
# ---------------------------------------------------------------------------

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ---------------------------------------------------------------------------
# Global constants
# ---------------------------------------------------------------------------

# Maximum total width (in characters) for a Markdown table row,
# including leading/trailing pipes and spaces.
MAX_TABLE_WIDTH = 120

# Minimum column width to avoid overly narrow columns
MIN_COL_WIDTH = 3

# Default SphereScript prefixes for highlighting (case-insensitive).
# These are common SphereScript property/tag prefixes.
# NOTE: "RETURN" removed from prefixes to avoid backticking prose like "Return Values"
#       It's handled specially in highlight_spherescript() when followed by number/operator.
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
    """
    Parse command-line arguments.

    Returns:
        Namespace with 'root' (directory path) and 'spherescript_prefixes' (list).
    """
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
    """
    Remove MediaWiki magic words like __FORCETOC__ from the text.
    Also removes simple escaped variants produced by Markdown (e.g. \\_\\_FORCETOC\\_\\_).
    """
    for word in MEDIAWIKI_MAGIC_WORDS:
        # Exact form
        text = text.replace(word, "")
        # Escaped underscores form (e.g. \_\_FORCETOC\_\_)
        escaped = word.replace("_", r"\_")
        text = text.replace(escaped, "")
    return text

def remove_spherescript_tags(text: str) -> str:
    """
    Remove <spherescript>...</spherescript> tags but keep their inner content.
    """
    return re.sub(
        r"<\s*spherescript\b[^>]*>(.*?)</\s*spherescript\s*>",
        lambda m: m.group(1),
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

def fix_broken_links(text: str) -> str:
    """
    Fix links broken by newlines, e.g. [map\npoints] -> [map points].
    """
    # [text\nmore] → [text more]
    text = re.sub(
        r"\[([^\]]*?)\n([^\]]*?)\]",
        lambda m: f"[{m.group(1).strip()} {m.group(2).strip()}]",
        text,
    )
    # (url\nrest) → (urlrest)
    text = re.sub(
        r"\(([^)]*?)\n([^)]*?)\)",
        lambda m: f"({m.group(1).strip()}{m.group(2).strip()})",
        text,
    )
    return text

def normalize_spacing_safely(text: str) -> str:
    """
    Only trim trailing whitespace on each line.
    Preserve leading whitespace and internal spacing entirely.
    """
    lines = [line.rstrip() for line in text.splitlines()]
    result = "\n".join(lines)
    if result and not result.endswith("\n"):
        result += "\n"
    return result

# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------

def line_is_table_row(line: str) -> bool:
    """
    Heuristic: check if a line looks like a Markdown table row.

    Used to:
    - Avoid inserting code fences inside tables.
    - Avoid adding extra backticks via inline highlighting inside tables.
    """
    stripped = line.lstrip()
    return stripped.startswith("|") and stripped.count("|") >= 2

def line_is_header(line: str) -> bool:
    """
    Check if a line is a Markdown header (starts with #).
    """
    return line.lstrip().startswith("#")

# ---------------------------------------------------------------------------
# Inline HTML → Markdown
# ---------------------------------------------------------------------------

def convert_inline_html(text: str) -> str:
    """
    Convert common inline HTML tags to Markdown equivalents, preserving
    existing Markdown syntax.
    """

    # 1. <strong> / <b> → **...**
    def strong_replacer(m: Match) -> str:
        inner = m.group(2).strip()
        if not inner:
            return ""
        return f"**{inner}**"

    text = re.sub(
        r"<\s*(strong|b)\b[^>]*>(.*?)</\s*(strong|b)\s*>",
        strong_replacer,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 2. <em> / <i> → *...*
    def em_replacer(m: Match) -> str:
        inner = m.group(2).strip()
        if not inner:
            return ""
        return f"*{inner}*"

    text = re.sub(
        r"<\s*(em|i)\b[^>]*>(.*?)</\s*(em|i)\s*>",
        em_replacer,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 3. <a href="url">text</a> → [text](url)
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

    # 4. Strip layout <div>/<span> but keep content
    text = re.sub(r"<\s*(div|span)\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</\s*(div|span)\s*>", "", text, flags=re.IGNORECASE)

    return text

# ---------------------------------------------------------------------------
# HTML tables → Markdown tables
# ---------------------------------------------------------------------------

def sanitize_cell_text(s: str) -> str:
    """
    Final sanitization for cell text:
    - Convert non-breaking spaces (\xa0) to regular spaces
    - Collapse multiple spaces
    - Strip leading/trailing whitespace
    """
    # Convert non-breaking spaces to regular spaces
    s = s.replace('\xa0', ' ')
    # Collapse multiple spaces
    s = re.sub(r'\s{2,}', ' ', s)
    return s.strip()

def cleanup_cell_content(s: str) -> str:
    """
    Clean content inside table cells.

    Steps:
    1. Strip outer whitespace.
    2. Convert <code>...</code> to backtick format.
    3. Normalize <br> variants and newlines to spaces so Markdown tables stay single-line per cell.
    4. Remove table structure tags: <tbody>, <tr>, <td>, <th>.
    5. Flatten <ul>/<li> lists inside cells into plain text.
    6. Remove nested <p> wrappers, keeping the inner text.
    7. Run inline HTML conversion for strong/em/links.
    8. Collapse redundant spaces and convert non-breaking spaces.
    9. Escape pipe characters so they do not split columns.
    """
    s = s.strip()

    # 2. <code>...</code> → `...` (backtick format for Markdown)
    s = re.sub(
        r"<\s*code\b[^>]*>(.*?)</\s*code\s*>",
        lambda m: f"`{m.group(1).strip()}`" if m.group(1).strip() else "",
        s,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 3. Newlines and <br> → spaces (tables must stay one logical line per cell)
    s = s.replace("\n", " ")
    s = re.sub(r"<\s*br\s*/?\s*>", " ", s, flags=re.IGNORECASE)

    # 4. Remove table-structure tags
    s = re.sub(r"</?tbody[^>]*>", "", s, flags=re.IGNORECASE)
    s = re.sub(r"</?(tr|td|th)\b[^>]*>", "", s, flags=re.IGNORECASE)

    # 5. Flatten <ul>/<li> lists inside cells to plain text
    # First, extract <li> contents
    def li_replacer(m: Match) -> str:
        inner = m.group(1).strip()
        return f"{inner}; " if inner else ""
    s = re.sub(
        r"<\s*li\b[^>]*>(.*?)</\s*li\s*>",
        li_replacer,
        s,
        flags=re.IGNORECASE | re.DOTALL,
    )
    # Remove remaining <ul>/<ol> tags
    s = re.sub(r"</?\s*(ul|ol)\b[^>]*>", "", s, flags=re.IGNORECASE)

    # 6. Remove <p> wrappers
    s = re.sub(
        r"<\s*p\b[^>]*>(.*?)</\s*p\s*>",
        lambda m: m.group(1).strip(),
        s,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 7. Inline HTML (strong, em, links)
    s = convert_inline_html(s)

    # 8. Final sanitization: collapse spaces, convert non-breaking spaces
    s = sanitize_cell_text(s)
    # Clean up leftover semicolon chains from list flattening
    s = re.sub(r";\s*;", ";", s)
    s = s.strip(" ;")

    # 9. Escape pipes to keep them inside cells
    s = s.replace("|", r"\|")

    return s.strip()

def convert_html_tables_to_markdown(text: str) -> str:
    """
    Convert all HTML <table>...</table> blocks to Markdown tables.

    Handles:
    - Tables with <th> (header) and <td> (data) cells
    - Nested content (lists, code, paragraphs) within cells
    - Column width normalization and scaling
    - Proper escaping of pipe characters within cells
    """

    def convert_single_table(m: Match) -> str:
        table_html = m.group(0)

        # Extract all <tr>...</tr> rows
        rows_html = re.findall(
            r"<\s*tr\b[^>]*>(.*?)</\s*tr\s*>",
            table_html,
            flags=re.IGNORECASE | re.DOTALL,
        )

        if not rows_html:
            # No rows found; return original HTML unchanged
            return table_html

        parsed_rows: List[List[str]] = []
        for row_html in rows_html:
            # Recursively convert nested tables if any
            row_html = convert_html_tables_to_markdown(row_html)

            # Try <th> cells first (header cells)
            th_cells = re.findall(
                r"<\s*th\b[^>]*>(.*?)</\s*th\s*>",
                row_html,
                flags=re.IGNORECASE | re.DOTALL,
            )
            if th_cells:
                cells = th_cells
            else:
                # Fallback to <td> cells (data cells)
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

        # Determine number of columns (max across all rows)
        max_cols = max(len(row) for row in parsed_rows) if parsed_rows else 1
        if max_cols == 0:
            max_cols = 1

        # Compute natural widths per column (before scaling)
        col_widths = [MIN_COL_WIDTH] * max_cols
        for row in parsed_rows:
            for col_idx, cell in enumerate(row):
                if col_idx < max_cols:
                    cell_str = str(cell)
                    col_widths[col_idx] = max(col_widths[col_idx], len(cell_str))

        # Compute total row width including pipes and spaces
        total_width = sum(col_widths) + max_cols * 3 + 1

        # If too wide, scale columns down proportionally
        if total_width > MAX_TABLE_WIDTH:
            excess = total_width - MAX_TABLE_WIDTH
            scale_factor = MAX_TABLE_WIDTH / max(total_width, 1)
            col_widths = [max(MIN_COL_WIDTH, int(w * scale_factor)) for w in col_widths]

        # FIXED: Get the first row as header, pad with empty strings if needed
        # Previously this was: header = parsed_rows + [""] * ... (WRONG - concatenated entire list)
        header_row = parsed_rows[0] if parsed_rows else []
        header_row = header_row + [""] * (max_cols - len(header_row))

        # Body rows: all rows after the first (or empty if only one row)
        body_rows = []
        for row in parsed_rows[1:]:
            padded = row + [""] * (max_cols - len(row))
            body_rows.append(padded)

        md_lines: List[str] = []

        # Header row
        header_line = "|"
        for i, cell in enumerate(header_row):
            if i >= len(col_widths):
                break
            cell_str = sanitize_cell_text(str(cell))
            # Truncate if exceeds column width
            if len(cell_str) > col_widths[i]:
                cell_str = cell_str[:col_widths[i]-1] + "…"
            padding = " " * max(0, col_widths[i] - len(cell_str))
            header_line += f" {cell_str}{padding} |"
        md_lines.append(header_line)

        # Separator row (dashes)
        sep_line = "|"
        for width in col_widths:
            sep_line += f" {'-' * width} |"
        md_lines.append(sep_line)

        # Body rows
        for row in body_rows:
            row_line = "|"
            for i, cell in enumerate(row):
                if i >= len(col_widths):
                    break
                cell_str = sanitize_cell_text(str(cell))
                # Truncate if exceeds column width
                if len(cell_str) > col_widths[i]:
                    cell_str = cell_str[:col_widths[i]-1] + "…"
                padding = " " * max(0, col_widths[i] - len(cell_str))
                row_line += f" {cell_str}{padding} |"
            md_lines.append(row_line)

        return "\n".join(md_lines)

    # Replace ALL <table>...</table> blocks with Markdown tables
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
    (Lists inside tables are already flattened in cleanup_cell_content.)
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
    Heuristic check whether a block of lines is already a valid Markdown table.

    A valid table has:
    - At least 2 lines (header + separator)
    - Header line contains |
    - Separator line contains | and -
    - All rows have the same number of columns
    """
    if len(lines) < 2:
        return False
    header = lines[0].strip()
    separator = lines[1].strip()
    if "|" not in header:
        return False
    if "-" not in separator or "|" not in separator:
        return False

    # Check consistent column count
    def count_cols(line: str) -> int:
        s = line.strip()
        if s.startswith("|"):
            s = s[1:]
        if s.endswith("|"):
            s = s[:-1]
        return len(s.split("|"))

    header_cols = count_cols(lines[0])
    for line in lines[1:]:
        if count_cols(line) != header_cols:
            return False

    return True

def normalize_single_table_block(block_lines: List[str]) -> List[str]:
    """
    Fix a malformed Markdown table and align columns with total width cap.

    This function handles Markdown tables that may have:
    - Inconsistent column counts across rows
    - Missing or malformed separator rows
    - Improper alignment/padding
    """
    rows: List[List[str]] = []
    for line in block_lines:
        s = line.strip()
        # Remove leading/trailing pipes if present
        if s.startswith("|"):
            s = s[1:]
        if s.endswith("|"):
            s = s[:-1]
        parts = s.split("|")
        # Sanitize each cell
        cells = [sanitize_cell_text(p) for p in parts]
        rows.append(cells)

    if not rows:
        return block_lines

    # Skip separator row (usually row index 1) when computing columns
    data_rows = [r for i, r in enumerate(rows) if i != 1 or not all(c.strip().replace('-', '') == '' for c in r)]

    max_cols = max(len(r) for r in data_rows) if data_rows else 1
    if max_cols == 0:
        max_cols = 1

    col_widths = [MIN_COL_WIDTH] * max_cols

    for row in data_rows:
        for col_idx, cell in enumerate(row):
            if col_idx < max_cols:
                col_widths[col_idx] = max(col_widths[col_idx], len(cell))

    total_width = sum(col_widths) + max_cols * 3 + 1
    if total_width > MAX_TABLE_WIDTH:
        scale_factor = MAX_TABLE_WIDTH / max(total_width, 1)
        col_widths = [max(MIN_COL_WIDTH, int(w * scale_factor)) for w in col_widths]

    # FIXED: Get first row as header, pad with empty strings if needed
    # Previously this was: header = rows + [""] * ... (WRONG - concatenated entire list)
    header_row = rows[0] if rows else []
    header_row = header_row + [""] * (max_cols - len(header_row))

    normalized: List[str] = []

    # Header row
    header_line = "|"
    for i, cell in enumerate(header_row):
        if i >= len(col_widths):
            break
        cell_str = sanitize_cell_text(cell)
        if len(cell_str) > col_widths[i]:
            cell_str = cell_str[:col_widths[i]-1] + "…"
        padding = " " * max(0, col_widths[i] - len(cell_str))
        header_line += f" {cell_str}{padding} |"
    normalized.append(header_line)

    # Separator row
    sep_line = "|"
    for width in col_widths:
        sep_line += f" {'-' * width} |"
    normalized.append(sep_line)

    # Body rows (skip the original separator if present)
    for idx, row in enumerate(rows[1:], start=1):
        # Skip if this looks like a separator row
        if all(c.strip().replace('-', '') == '' for c in row):
            continue

        row_line = "|"
        padded_row = row + [""] * (max_cols - len(row))
        for i, cell in enumerate(padded_row):
            if i >= len(col_widths):
                break
            cell_str = sanitize_cell_text(cell)
            if len(cell_str) > col_widths[i]:
                cell_str = cell_str[:col_widths[i]-1] + "…"
            padding = " " * max(0, col_widths[i] - len(cell_str))
            row_line += f" {cell_str}{padding} |"
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
        # Detect potential table start: line with | followed by line with - and |
        if "|" in line and i + 1 < n and "-" in lines[i + 1] and "|" in lines[i + 1]:
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
# SphereScript highlighting (outside fenced code)
# ---------------------------------------------------------------------------

def highlight_spherescript(text: str, prefixes: List[str]) -> str:
    """
    Highlight SphereScript constructs using backticks, but
    ONLY outside existing fenced code blocks, outside tables,
    and NOT inside Markdown links or headers.
    """
    prefixes_pattern = "|".join(re.escape(p.lower()) for p in prefixes)
    cf_pattern = r"^\s*(IF|ELSEIF|ELSE|ENDIF|WHILE|ENDWHILE|FOR\w*|ENDFOR|DOSWITCH|ENDDO)\b"

    lines = text.splitlines()
    out_lines: List[str] = []
    in_fence = False

    for line in lines:
        stripped = line.strip()

        # Toggle fence on lines starting with ```
        if stripped.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue

        if in_fence:
            out_lines.append(line)
            continue

        # Do not touch table rows
        if line_is_table_row(line):
            out_lines.append(line)
            continue

        # Do not touch Markdown header lines (## Header)
        if line_is_header(line):
            out_lines.append(line)
            continue

        # 1. Prefix-based identifiers (TAG., DEF., etc.)
        def prefix_replacer(m: Match) -> str:
            return f"`{m.group(0)}`"

        line = re.sub(
            rf"\b({prefixes_pattern})[A-Za-z0-9_.]*",
            prefix_replacer,
            line,
            flags=re.IGNORECASE,
        )

        # 2. Control-flow keywords at start of line
        def control_flow_replacer(m: Match) -> str:
            full = m.group(0)
            keyword = m.group(1)
            return full.replace(keyword, f"`{keyword}`", 1)

        line = re.sub(
            cf_pattern,
            control_flow_replacer,
            line,
            flags=re.IGNORECASE,
        )

        # 3. Bracket block at beginning of line: [SOMETHING]
        #    BUT only if NOT followed by ( which indicates a Markdown link
        #    FIXED: Added negative lookahead (?!\s*\() to avoid breaking links
        line = re.sub(
            r"^\s*(\[[^\]\n]+\])(?!\s*\()",
            lambda m: f"`{m.group(1)}`",
            line,
        )

        # 4. Handle RETURN specifically: only backtick when followed by number, operator, or end of line
        #    This avoids backticking "Return" in prose like "Return Values" or "Return the result"
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
    """
    Detect likely SphereScript lines and wrap contiguous runs in ``` fences.

    Conservative heuristics:
    - Never start/close fences on Markdown table rows.
    - Do NOT use prefix-based heuristics here (only explicit code-ish patterns).
    """
    cf_start_re = re.compile(r"^\s*(IF|WHILE|FOR\w*|DOSWITCH)\b", re.IGNORECASE)
    cf_end_re = re.compile(r"^\s*(ENDIF|ENDWHILE|ENDFOR|ENDDO)\b", re.IGNORECASE)

    lines = text.splitlines()
    result: List[str] = []

    in_block = False       # Currently inside a ```
    in_md_fence = False    # Inside an existing markdown fence (any language)
    in_comment_block = False
    cf_level = 0

    for line in lines:
        stripped = line.strip()

        # Respect existing markdown fences
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

        # Never fence table rows
        if line_is_table_row(line):
            if in_block:
                result.append("```")
                in_block = False
            result.append(line)
            continue

        # Never fence Markdown headers
        if line_is_header(line):
            if in_block:
                result.append("```")
                in_block = False
            result.append(line)
            continue

        is_code = False

        # Multi-line C-style comments /* ... */
        if not in_comment_block and "/*" in stripped and "*/" not in stripped:
            in_comment_block = True
            is_code = True
        elif in_comment_block:
            is_code = True
            if "*/" in stripped:
                in_comment_block = False

        # Single-line comments
        if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*/"):
            is_code = True

        # Control-flow block tracking
        if cf_start_re.match(stripped):
            cf_level += 1
            is_code = True
        elif cf_end_re.match(stripped):
            is_code = True
            cf_level = max(cf_level - 1, 0)
        elif cf_level > 0:
            is_code = True

        # Triggers/labels starting with @ (but not if it looks like a Markdown link)
        if not is_code and stripped.startswith("@") and not re.match(r"^\[@[^\]]+\]\(", stripped):
            is_code = True

        # Simple assignment pattern: NAME = value (not a list item, avoid prose)
        if (not is_code and
            re.match(r"^\s*[\w\.\[\]]+\s*=", stripped) and
            not stripped.startswith("- ") and
            len(stripped.split()) <= 4):
            is_code = True

        # Manage our own fenced block state
        if is_code and not in_block:
            result.append("```")
            in_block = True
        elif not is_code and in_block:
            result.append("```")
            in_block = False

        result.append(line)

    # Close fence if still open at EOF
    if in_block:
        result.append("```")

    return "\n".join(result)

# ---------------------------------------------------------------------------
# Remove <code> html tag (outside tables)
# ---------------------------------------------------------------------------

def convert_inline_code_outside_tables(text: str) -> str:
    """
    Simple global <code> → `...` for non‑table content.
    HTML tables are handled separately by cleanup_cell_content.
    """
    return re.sub(
        r"<\s*code\b[^>]*>(.*?)</\s*code\s*>",
        lambda m: f"`{m.group(1).strip()}`" if m.group(1).strip() else "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

# ---------------------------------------------------------------------------
# Main processing pipeline
# ---------------------------------------------------------------------------

def process_markdown(text: str, spherescript_prefixes: List[str]) -> str:
    """
    Apply all cleanup and normalization steps to a single Markdown document.

    Order is important:
    1. Remove MediaWiki magic + spherescript tags
    2. Convert HTML tables (flatten inner lists, code, etc.)
    3. Convert remaining HTML lists outside tables
    4. Convert inline <code> outside tables
    5. Convert inline HTML
    6. Fix broken links (e.g. [map\npoints])
    7. Normalize malformed Markdown tables
    8. Fence SphereScript code blocks (very conservative)
    9. Highlight SphereScript inline (outside fences and tables)
    10. Trailing-whitespace cleanup
    """
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
    text = normalize_spacing_safely(text)
    return text

# ---------------------------------------------------------------------------
# Diff output
# ---------------------------------------------------------------------------

def show_diff(original: str, cleaned: str, path: Path) -> None:
    """
    Print a colorized unified diff for a file, with clear separators and spacing.
    """
    orig_lines = original.splitlines(keepends=True)
    new_lines = cleaned.splitlines(keepends=True)

    print()
    print(CYAN + "═" * 88 + RESET)
    print(CYAN + f"File: {path}" + RESET)
    print(CYAN + "═" * 88 + RESET)
    print()

    for line in difflib.unified_diff(
        orig_lines,
        new_lines,
        fromfile=str(path),
        tofile=str(path),
        lineterm="",
    ):
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
    """
    Read, process, and possibly overwrite a single .md file.
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

def main() -> None:
    """
    Entry point: walk directory tree and process all .md files.
    """
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
