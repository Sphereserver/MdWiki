import os
import subprocess
from pathlib import Path

# TODO: add a threadpool executor!

def convert_file(input_path, output_path):
    """Converts a single file from mediawiki to gfm using pandoc."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            wikitext = f.read()

        process = subprocess.run(
            ['pandoc', '-f', 'mediawiki', '-t', 'gfm'], # GitHub Flavored Markdown
            input=wikitext,
            text=True,
            capture_output=True,
            check=True,
            timeout=30
        )
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(process.stdout)
        
        print(f"Successfully converted '{input_path}' to '{output_path}'")
        return True

    except FileNotFoundError:
        print(f"FATAL: `pandoc` command not found. Please install pandoc and ensure it's in your PATH.")
        return False
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        print(f"Error converting '{input_path}': {e.stderr}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while converting '{input_path}': {e}")
        return False

def main(source_dir, dest_dir):
    """
    Walks through the source directory, converts each .txt file from mediawiki
    to markdown, and saves it in the destination directory, preserving the
    folder structure.
    """
    print(f"Starting conversion from '{source_dir}' to '{dest_dir}'...")
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)

    if not source_path.is_dir():
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".txt"):
                source_file_path = Path(root) / file
                relative_path = source_file_path.relative_to(source_path)
                dest_file_path = (dest_path / relative_path).with_suffix(".md")
                
                convert_file(source_file_path, dest_file_path)

    print("Conversion process finished.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python convert_mediawiki_to_md.py <source_directory> <destination_directory>")
    else:
        main(sys.argv[1], sys.argv[2])
