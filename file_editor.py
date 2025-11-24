import argparse
import os

def replace_in_file(filepath, old_string, new_string):
    """
    Reads a file, performs a literal string replacement, and writes the changes back.
    Reports the number of occurrences replaced.
    """
    if not os.path.exists(filepath):
        print(f"ERROR: File not found at path: {filepath}")
        return False

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Count occurrences before replacing
        initial_count = content.count(old_string)

        if initial_count == 0:
            print(f"FAILURE: 0 occurrences found for old_string in {filepath}. No changes made.")
            # Print the old string clearly for debugging
            print("--- Old String Provided ---")
            print(old_string)
            print("-------------------------")
            return False

        # Perform replacement
        new_content = content.replace(old_string, new_string)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"SUCCESS: Replaced {initial_count} occurrence(s) in {filepath}.")
        return True

    except Exception as e:
        print(f"ERROR: An unexpected error occurred while processing {filepath}: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Reliable utility for finding and replacing literal strings in files."
    )
    parser.add_argument('filepath', type=str, help='The path to the file to be edited.')
    parser.add_argument('--old', type=str, required=True, help='The literal string to find and replace.')
    parser.add_argument('--new', type=str, required=True, help='The replacement string.')

    args = parser.parse_args()

    # We exit with a non-zero code on failure so shell scripts can check status
    if not replace_in_file(args.filepath, args.old, args.new):
        sys.exit(1)

