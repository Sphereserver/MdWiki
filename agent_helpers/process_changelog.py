
import re
import os
import argparse
from datetime import datetime

def parse_changelog_entry(entry_text):
    """Parses a single changelog entry block."""
    lines = entry_text.strip().split('\n')
    if not lines:
        return None

    header_match = re.match(r'(\d{2}-\d{2}-\d{4}),\s*(.+)', lines[0])
    if not header_match:
        return None

    date = header_match.group(1)
    author = header_match.group(2)
    changes = []
    for line in lines[1:]:
        line = line.strip()
        if line.startswith('- '):
            changes.append(line[2:].strip())
        elif line: # Add continuation lines to the last change
            if changes:
                changes[-1] += " " + line
            else:
                changes.append(line) # Should not happen with valid format, but for safety
    return {'date': date, 'author': author, 'changes': changes, 'raw': entry_text}

def load_changelog_file(filepath):
    """Loads and parses the Changelog.txt file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    main_sections = re.split(r'^----.*$', content, flags=re.MULTILINE)

    entries = []
    for section in main_sections:
        if not section.strip():
            continue
        individual_entry_blocks = re.split(r'^(?=\d{2}-\d{2}-\d{4},\s*.+$)', section, flags=re.MULTILINE)
        for block in individual_entry_blocks:
            if block.strip():
                entry = parse_changelog_entry(block)
                if entry:
                    entries.append(entry)
    return entries






def get_entry_header(entry):
    return f"{entry['date']}, {entry['author']}"


def load_progress_file_entries(filepath):
    """Loads entries from changelog_progress.txt, preserving their raw text and processed status."""
    if not os.path.exists(filepath):
        return []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by the '---' separator
    # The regex ensures that '---' is considered a separator only when it's on its own line.
    entry_blocks_raw = re.split(r'^\s*---\s*$', content, flags=re.MULTILINE)
    
    entries = []
    for block_raw in entry_blocks_raw:
        block_raw = block_raw.strip()
        if not block_raw:
            continue

        # Check if the block is processed (has strike-through markdown)
        is_processed = False
        # A simple check: if any line starts and ends with '~~', consider the block processed.
        # This might need refinement if the strike-through can be partial or on specific lines.
        # For now, let's assume the entire entry block gets struck through.
        if block_raw.startswith('~~') and block_raw.endswith('~~'):
            is_processed = True
            block_content = block_raw[2:-2].strip() # Remove '~~' for parsing content
        else:
            block_content = block_raw
        
        # Try to parse the header to get date and author, similar to parse_changelog_entry
        header_match = re.match(r'(\d{2}-\d{2}-\d{4}),\s*(.+)', block_content.split('\n')[0])
        if header_match:
            header_date = header_match.group(1)
            header_author = header_match.group(2)
            entry_header = f"{header_date}, {header_author}"
        else:
            entry_header = None # This block might not be a valid changelog entry (e.g., static text)

        entries.append({
            'raw_text': block_raw,
            'content': block_content,
            'header': entry_header,
            'is_processed': is_processed
        })
    return entries


def mark_entries_as_processed(filepath, entries_to_mark):
    """
    Marks specified entries in the changelog_progress.txt file with strike-through.
    entries_to_mark is a list of header strings (e.g., '01-06-2019, Nolok').
    """
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found for marking entries.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified_lines = []
    batch_found = False
    
    # Compile a regex to match the headers we need to mark
    headers_regex = re.compile(r'|'.join([re.escape(h) for h in entries_to_mark]))

    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this line is a header that needs to be marked
        # We need to be careful here not to accidentally mark '---' as part of an entry
        if headers_regex.search(line) and not line.strip().startswith('---'):
            batch_found = True
            # Find the start of the entry block (could be this line or earlier if there's no ---)
            entry_start_idx = i
            while entry_start_idx > 0 and not lines[entry_start_idx - 1].strip() == '---':
                entry_start_idx -= 1
            
            # Find the end of the entry block (before the next --- or EOF)
            entry_end_idx = i
            while entry_end_idx < len(lines) and not lines[entry_end_idx].strip() == '---':
                entry_end_idx += 1
            
            # Mark the entire block with strike-through
            modified_lines.append('~~\n') # Start strike-through
            for j in range(entry_start_idx, entry_end_idx):
                # Only add the line if it's not already marked or not an empty line
                current_line_strip = lines[j].strip()
                if not current_line_strip.startswith('~~') and current_line_strip != '---':
                    modified_lines.append(lines[j])
            modified_lines.append('~~\n') # End strike-through
            
            i = entry_end_idx # Move index past this processed block
            continue # Continue to the next line after the block
        else:
            modified_lines.append(line)
        i += 1
    
    if not batch_found:
        print("Warning: No entries from the last batch were found to mark as processed in changelog_progress.txt.")
        return

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(modified_lines)
    print(f"Marked {len(entries_to_mark)} entries as processed in {filepath}.")


def main():
    parser = argparse.ArgumentParser(description="Process SphereServer Changelog entries for wiki updates.")
    parser.add_argument("--start-point-header", type=str,
                        help="Changelog entry header (e.g., '01-06-2019, Nolok') to start processing from.")
    parser.add_argument("--mark-as-processed", action="store_true",
                        help="Mark the last processed batch of entries as complete in changelog_progress.txt.")
    args = parser.parse_args()

    changelog_filepath = 'Changelog.txt' # Assuming Changelog.txt is in the root directory
    progress_filepath = os.path.join(os.path.dirname(__file__), 'changelog_progress.txt')

    # --- Handle marking entries as processed ---
    if args.mark_as_processed:
        try:
            tmp_headers_filepath = os.path.join(os.path.dirname(__file__), '.last_processed_batch_headers.tmp')
            with open(tmp_headers_filepath, 'r', encoding='utf-8') as f:
                last_batch_headers = [line.strip() for line in f if line.strip()]
            if last_batch_headers:
                mark_entries_as_processed(progress_filepath, last_batch_headers)
                os.remove(tmp_headers_filepath)
            else:
                print("No last processed batch found to mark.")
        except FileNotFoundError:
            print("No previous batch found to mark as processed. Run the script first to get a batch.")
        return

    # --- Processing new entries ---
    start_point_header = args.start_point_header
    if not start_point_header:
        print("Error: --start-point-header is required when not marking entries as processed.")
        return

    all_changelog_entries = load_changelog_file(changelog_filepath)
    progress_file_entries = load_progress_file_entries(progress_filepath)

    entries_to_process = []
    start_collecting = False
    batch_size = 5
    current_batch_count = 0
    batch_headers_for_progress = []

    for entry in all_changelog_entries:
        entry_header = get_entry_header(entry)

        # Find the corresponding entry in the progress file to check if it's processed
        corresponding_progress_entry = next((p_entry for p_entry in progress_file_entries if p_entry['header'] == entry_header), None)
        is_processed_in_progress_file = corresponding_progress_entry and corresponding_progress_entry['is_processed']
        
        if entry_header == start_point_header:
            start_collecting = True # Start collecting entries from this point onwards

        # Only add entries that are after the start_point_header (or is the start_point_header)
        # and haven't been processed yet, and we haven't filled the batch.
        if start_collecting and not is_processed_in_progress_file and current_batch_count < batch_size:
            entries_to_process.append(entry)
            batch_headers_for_progress.append(entry_header)
            current_batch_count += 1
        elif current_batch_count >= batch_size:
            # We've filled the current batch, stop collecting
            break
            
    if not entries_to_process:
        print("No new changelog entries to process from the specified start point, or all are processed.")
        return

    print(f"Found {len(entries_to_process)} new entries to process in this batch:")
    
    for entry in entries_to_process:
        entry_header = get_entry_header(entry)
        print(f"  - Processing: {entry_header}")
        
        # --- WIKI UPDATE LOGIC GOES HERE ---
        print("    Changes to integrate into wiki:")
        for change in entry['changes']:
            print(f"      - {change}")
        # --- END WIKI UPDATE LOGIC ---
    
    # Save the headers of the current batch to a temporary file
    # This file will be read when --mark-as-processed is used in the next run.
    with open('.last_processed_batch_headers.tmp', 'w', encoding='utf-8') as f:
        for header in batch_headers_for_progress:
            f.write(header + '\n')

    print(f"\nBatch of {len(entries_to_process)} entries displayed. After updating the wiki, run with --mark-as-processed to update {progress_filepath}.")

if __name__ == '__main__':
    main()
