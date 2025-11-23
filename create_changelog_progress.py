import re

# Read the full changelog content
with open('Changelog.txt', 'r', encoding='utf-8') as f:
    changelog_content = f.read()

# Regex to find lines starting with a date and author,
# potentially including porting info or multiple commits.
# Example patterns:
# "DD-MM-YYYY, Author"
# "DD-MM-YYYY / DD-MM-YYYY (N commits), Author"
date_author_pattern = re.compile(r'^\d{2}-\d{2}-\d{4}(?:\/\s\d{1,2}-\d{1,2}-\d{4})?(?:\s\(\d+\scommits\))?,\s[A-Za-z\s]+.*')

entries = []
current_entry_lines = []
in_changelog_section = False

for line in changelog_content.splitlines():
    if not in_changelog_section:
        # Skip initial header lines until the first actual changelog entry is found
        if date_author_pattern.match(line):
            in_changelog_section = True
            current_entry_lines.append(line)
        continue

    if date_author_pattern.match(line):
        if current_entry_lines:
            entries.append("\n".join(current_entry_lines).strip())
        current_entry_lines = [line]
    else:
        current_entry_lines.append(line)

# Add the last entry
if current_entry_lines:
    entries.append("\n".join(current_entry_lines).strip())

# Filter out any entries that are just empty or only contain whitespace
filtered_entries = [entry for entry in entries if entry]

# Write to changelog_progress.txt
with open('changelog_progress.txt', 'w', encoding='utf-8') as f:
    for entry in filtered_entries:
        f.write(entry + "\n---\n") # Use '---' as a clear delimiter between entries

print(f"Extracted {len(filtered_entries)} entries to changelog_progress.txt")