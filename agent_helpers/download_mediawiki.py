import re
import os
import requests
from urllib.parse import quote, unquote
import concurrent.futures
import threading
from pathlib import Path

BASE_URL = "https://wiki.spherecommunity.net/index.php"
OUTPUT_DIR = Path("wiki_mediawiki_orig")
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
    links = re.findall(r'\[\[:?([^|\]]+)(?:\|[^\\\]]*)?\]\]', wikitext)
    
    # Filter out links to sections on the same page and external-like links
    unique_links = {link.strip() for link in links if not link.startswith('#') and '://' not in link}
    return list(unique_links)

def download_and_save_wikitext(page_title):
    """
    Downloads the raw wikitext for a given page and saves it to the OUTPUT_DIR.
    Returns a list of new page titles to crawl.
    """
    sanitized_name = sanitize_title(page_title)
    if not sanitized_name:
        print(f"Skipping '{page_title}' due to empty sanitized name.", flush=True)
        return []
        
    print(f"Downloading: '{page_title}' -> '{sanitized_name}.txt'", flush=True)
    
    file_path = OUTPUT_DIR / f"{sanitized_name}.txt"
    
    if file_path.exists():
        print(f"  -> Already exists, skipping download: {file_path}", flush=True)
        with open(file_path, 'r', encoding='utf-8') as f:
            wikitext = f.read()
        return find_links(wikitext)


    wikitext = get_wikitext(page_title)
    if wikitext:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(wikitext)
            print(f"  -> Downloaded and saved: {file_path}", flush=True)
            return find_links(wikitext)
        except Exception as e:
            print(f"  -> Error saving '{page_title}': {e}", flush=True)
    return []


def main():
    """Main function to crawl and download the wiki wikitext."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # A queue for pages to visit
    pages_to_visit = ["Main_Page"]
    
    print(f"Starting wiki wikitext download. Initial pages to visit: {pages_to_visit}", flush=True)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while pages_to_visit:
            current_batch = pages_to_visit[:] # Take a snapshot of current pages to visit
            pages_to_visit = [] # Clear the queue for the next iteration
            print(f"Batch size: {len(current_batch)}. Total processed so far: {len(processed_pages)}", flush=True)

            # Add current_batch pages to processed_pages to prevent reprocessing within the same batch
            with processed_pages_lock:
                for page in current_batch:
                    processed_pages.add(page)

            future_to_page = {
                executor.submit(download_and_save_wikitext, page): page for page in current_batch
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
    print("Wiki wikitext download complete.", flush=True)
    print(f"Total pages downloaded: {len(processed_pages)}", flush=True)
    print("--------------------", flush=True)

if __name__ == "__main__":
    # Add the initial page to the set of processed pages
    with processed_pages_lock: # Ensure thread safety even for initial add
        processed_pages.add("Main_Page")
    main()