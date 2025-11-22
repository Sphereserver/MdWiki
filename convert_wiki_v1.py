import re
import subprocess
import os
import requests
from urllib.parse import quote, unquote
import concurrent.futures
import shutil
import threading

BASE_URL = "https://wiki.spherecommunity.net/index.php"
OUTPUT_DIR = "wiki_markdown"
OLD_OUTPUT_DIR = "wiki_markdown_v1"
MAX_WORKERS = 10

# A thread-safe set to keep track of visited pages
visited_lock = threading.Lock()
visited = set()

# A thread-safe list for pages to visit
to_visit_lock = threading.Lock()
to_visit = ["Main_Page"]

def sanitize_title(title):
    """Sanitizes a title to be a valid filename."""
    return re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_').replace('/', '_')

def get_wikitext(page_title):
    """Fetches the raw wikitext for a given page title."""
    encoded_title = quote(page_title)
    url = f"{BASE_URL}?title={encoded_title}&action=raw"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page_title}: {e}")
        return None

def find_links(wikitext):
    """Finds all MediaWiki links in the given wikitext."""
    links = re.findall(r'\[\[:?([^|\]]+)(?:\|[^|\]]+)?\]\]', wikitext)
    return [link for link in links if not link.startswith('#')]

def convert_to_markdown(wikitext, page_title):
    """Converts wikitext to Markdown using pandoc."""
    sanitized = sanitize_title(page_title)
    markdown_filename = os.path.join(OUTPUT_DIR, f"{sanitized}.md")
    
    try:
        # Use 'markdown' format which produces [text](link "wikilink")
        process = subprocess.run(
            ['pandoc', '-f', 'mediawiki', '-t', 'markdown'],
            input=wikitext,
            text=True,
            capture_output=True,
            check=True
        )
        with open(markdown_filename, 'w', encoding='utf-8') as f:
            f.write(process.stdout)
        # print(f"Converted '{page_title}' to '{markdown_filename}'")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error converting page {page_title}: {e}")
        return False

def process_page(page_title):
    """Processes a single wiki page: copy if exists, else fetch, convert, and find new links."""
    global visited, to_visit

    with visited_lock:
        if page_title in visited:
            return
        visited.add(page_title)
    
    print(f"Processing: {page_title}")

    sanitized = sanitize_title(page_title)
    if not sanitized:
        return

    old_file_path = os.path.join(OLD_OUTPUT_DIR, f"{sanitized}.md")
    if os.path.exists(old_file_path):
        shutil.copy(old_file_path, os.path.join(OUTPUT_DIR, f"{sanitized}.md"))
        # To find new links, we must fetch the source anyway.
        # This caching only saves the conversion step, not the fetch.
        # A better cache would store the wikitext.
    
    wikitext = get_wikitext(page_title)
    if not wikitext:
        return

    if not convert_to_markdown(wikitext, page_title):
        return

    new_links = find_links(wikitext)
    with to_visit_lock:
        for link in new_links:
            with visited_lock:
                if link not in visited:
                    to_visit.append(link)

def post_process_links():
    """Fixes internal links in all converted markdown files."""
    print("\nPost-processing links...")
    for filename in os.listdir(OUTPUT_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(OUTPUT_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            def replace_link(match):
                text = match.group(1)
                link = match.group(2)
                
                link = unquote(link)

                if not re.match(r"^[a-zA-Z]+://", link) and not link.startswith("#"):
                    page_name = link.split(' ')[0]
                    sanitized_link = sanitize_title(page_name) + ".md"
                    return f'[{text}](./{sanitized_link})'
                return match.group(0)

            content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    print("Link processing complete.")

def main():
    """Main function to crawl the wiki and convert pages using a thread pool."""
    global to_visit, visited
    
    # Use a queue-like structure for visiting pages
    page_queue = ["Main_Page"]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(process_page, page) for page in page_queue}
        
        while futures:
            done, futures = concurrent.futures.wait(
                futures, return_when=concurrent.futures.FIRST_COMPLETED
            )
            
            # Process new links found by completed tasks
            # This is tricky because we can't easily get return values with new links
            # A shared queue for new links is better.

    # A simpler loop that grows the to_visit list dynamically
    processed_count = 0
    while processed_count < len(to_visit):
        page_to_process = to_visit[processed_count]
        processed_count += 1
        
        with visited_lock:
            if page_to_process in visited:
                continue
        
        process_page(page_to_process)


    # The thread pool logic was a bit flawed for a growing list of tasks.
    # Let's try a simpler approach for now.
    
    # Initial page
    process_page("Main_Page")

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Use a copy of to_visit for iteration because it will be modified
        while True:
            with to_visit_lock:
                pages_to_submit = [p for p in to_visit if p not in visited]
            
            if not pages_to_submit:
                break
            
            # Submit new tasks
            future_to_page = {executor.submit(process_page, page): page for page in pages_to_submit}

            # Wait for tasks to complete
            for future in concurrent.futures.as_completed(future_to_page):
                page = future_to_page[future]
                try:
                    future.result()
                except Exception as exc:
                    print(f'{page} generated an exception: {exc}')

    post_process_links()


if __name__ == "__main__":
    main()