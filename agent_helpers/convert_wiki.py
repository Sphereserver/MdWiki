import re
import subprocess
import os
import requests
from urllib.parse import quote, unquote
import concurrent.futures
import shutil
import threading
from pathlib import Path

BASE_URL = "https://wiki.spherecommunity.net/index.php"
OUTPUT_DIR = Path("wiki_markdown")
OLD_OUTPUT_DIR = Path("wiki_markdown_v1")
MAX_WORKERS = 10

# Thread-safe set to keep track of pages being processed or queued
processed_pages = set()
processed_pages_lock = threading.Lock()

def sanitize_title(title):
    """Sanitizes a title to be a valid filename."""
    # Remove namespace prefixes if present (e.g., "Category:")
    if ':' in title:
        title = title.split(':', 1)[1]
    
    # Basic sanitization
    sanitized = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
    
    # Avoid creating files with names that are too long
    return sanitized[:100]

def get_wikitext(page_title):
    """Fetches the raw wikitext for a given page title."""
    encoded_title = quote(page_title)
    url = f"{BASE_URL}?title={encoded_title}&action=raw"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"  -> Error fetching '{page_title}': {e}", flush=True)
        return None

def find_links(wikitext):
    """Finds all unique MediaWiki links in the given wikitext."""
    # This regex captures the link target, which is the first part before a '|'
    links = re.findall(r'\[\[:?([^|\]]+)(?:\|[^\]]*)?\]\]', wikitext)
    
    # Filter out links to sections on the same page and external-like links
    unique_links = {link.strip() for link in links if not link.startswith('#') and '://' not in link}
    return list(unique_links)

def convert_and_save(wikitext, page_title):
    """Converts wikitext to Markdown using pandoc and saves it."""
    sanitized_name = sanitize_title(page_title)
    if not sanitized_name:
        return False
        
    markdown_path = OUTPUT_DIR / f"{sanitized_name}.md"

    try:
        process = subprocess.run(
            ['pandoc', '-f', 'mediawiki', '-t', 'gfm'], # Using GitHub-Flavored Markdown
            input=wikitext,
            text=True,
            capture_output=True,
            check=True,
            timeout=30
        )
        
        # Post-process links after pandoc conversion
        markdown_content = post_process_pandoc_links(process.stdout)

        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        return True
    except FileNotFoundError:
        print("FATAL: `pandoc` command not found. Please install pandoc and ensure it's in your PATH.", flush=True)
        return False
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        print(f"  -> Error converting '{page_title}' with pandoc: {e}", flush=True)
        return False

def run_pandoc(wikitext):
    """Runs pandoc to convert wikitext to markdown."""
    try:
        process = subprocess.run(
            ['pandoc', '-f', 'mediawiki', '-t', 'gfm'],
            input=wikitext,
            text=True,
            capture_output=True,
            check=True,
            timeout=30
        )
        return process.stdout
    except FileNotFoundError:
        print("FATAL: `pandoc` command not found. Please install pandoc and ensure it's in your PATH.", flush=True)
        return None
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        print(f"  -> Error converting with pandoc: {e}", flush=True)
        return None

def post_process_pandoc_links(markdown_text):
    """Adjusts pandoc-generated links to be relative file links."""
    
    # Pandoc creates links like: [link text](Title "wikilink")
    # We need to convert "Title" into "./Sanitized_Title.md"
    def replace_func(match):
        text = match.group(1)
        url = match.group(2)
        title = match.group(3)

        if title == "wikilink" and '://' not in url:
            # This is an internal link, format it correctly
            sanitized_link = sanitize_title(unquote(url))
            if not sanitized_link:
                return text # Return just text if link is invalid
            return f'[{text}](./{sanitized_link}.md)'
        else:
            # Keep external links or other links as is
            return match.group(0)

    # Regex to find [text](url "wikilink") - allowing for optional space before "wikilink"
    processed_text = re.sub(r'\[([^\]]+)\]\(([^)]+)\s?"([^"]+)"\)', replace_func, markdown_text)
    return processed_text


def process_page(page_title):
    """
    Processes a single wiki page.
    1. Checks if a pre-converted file exists and uses it (cache).
    2. If not, fetches the wikitext from the web and converts it.
    3. Fixes internal links.
    4. Finds all new links on the page to be processed next.
    Returns a list of new page titles to crawl.
    """
    sanitized_name = sanitize_title(page_title)
    if not sanitized_name:
        print(f"Skipping '{page_title}' due to empty sanitized name.", flush=True)
        return []
        
    print(f"Processing: '{page_title}' -> '{sanitized_name}.md'", flush=True)
    
    old_file_path = OLD_OUTPUT_DIR / f"{sanitized_name}.md"
    new_file_path = OUTPUT_DIR / f"{sanitized_name}.md"
    
    markdown_content = None
    wikitext = None

    if old_file_path.exists():
        with open(old_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        print(f"  -> Found in cache: {old_file_path}", flush=True)
    else:
        wikitext = get_wikitext(page_title)
        if wikitext:
            markdown_content = run_pandoc(wikitext)

    if markdown_content:
        fixed_content = post_process_pandoc_links(markdown_content)
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)

    # if wikitext is not fetched yet, fetch it for links
    if wikitext is None:
        wikitext = get_wikitext(page_title)

    if wikitext:
        return find_links(wikitext)
    return []


def main():
    """Main function to crawl and convert the wiki."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # A queue for pages to visit
    pages_to_visit = ["Main_Page"]
    
    print(f"Starting wiki conversion. Initial pages to visit: {pages_to_visit}", flush=True)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while pages_to_visit:
            current_batch = pages_to_visit[:] # Take a snapshot of current pages to visit
            pages_to_visit = [] # Clear the queue for the next iteration
            print(f"Batch size: {len(current_batch)}. Total processed so far: {len(processed_pages)}", flush=True)

            future_to_page = {
                executor.submit(process_page, page): page for page in current_batch
            }
            
            for future in concurrent.futures.as_completed(future_to_page):
                page_title = future_to_page[future]
                try:
                    new_links = future.result()
                    
                    # For each new link, add it to the queue if not already processed
                    with processed_pages_lock:
                        for link in new_links:
                            if link not in processed_pages:
                                pages_to_visit.append(link)
                                processed_pages.add(link)

                except Exception as e:
                    print(f"!! Exception processing '{page_title}': {e}", flush=True)
    
    print("\n--------------------", flush=True)
    print("Wiki conversion complete.", flush=True)
    print(f"Total pages processed: {len(processed_pages)}", flush=True)
    print("--------------------", flush=True)

if __name__ == "__main__":
    # Add the initial page to the set of processed pages
    with processed_pages_lock: # Ensure thread safety even for initial add
        processed_pages.add("Main_Page")
    main()
