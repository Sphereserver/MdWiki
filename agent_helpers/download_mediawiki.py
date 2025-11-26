#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MediaWiki Downloader & Crawler (Wikitext Only)
==============================================

This script merges the functionality of an API-based exporter and a recursive link crawler.
It allows you to download a MediaWiki site by either:
1. (API Mode) Listing all pages via the MediaWiki API and downloading them.
2. (Crawler Mode) Starting from a root page, finding all links, and recursively downloading children.

Key Features:
- Recursive folder structure for crawler (Parent/Child hierarchy).
- Multithreading for the crawler.
- Category-based organization for API mode.
- Downloads raw wikitext only (no Markdown conversion).

Usage:
    # Crawler Mode (default): Start at Main_Page, create subfolders for children
    python3 mediawiki_merged.py --url "https://wiki.example.com/index.php" --mode crawler

    # Crawler Mode: Flat output (no subfolders)
    python3 mediawiki_merged.py --url "https://wiki.example.com/index.php" --mode crawler --flat-output

    # API Mode: Download all pages found via API
    python3 mediawiki_merged.py --url "https://wiki.example.com/api.php" --mode api

Dependencies:
    pip install requests
"""

import argparse
import concurrent.futures
import logging
import re
import threading
import sys
from pathlib import Path
from typing import List, Optional, Set, Tuple
from urllib.parse import quote

import requests

# Configure logging to stdout with timestamps
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

class MediaWikiTool:
    """
    Base class containing shared utilities for sanitization,
    request handling, and file writing.
    """
    def __init__(self, output_dir: str, user_agent: str = "MediaWikiDownloader/2.0"):
        self.output_dir = Path(output_dir)
        self.user_agent = user_agent
        self.session = requests.Session()
        self.session.headers["User-Agent"] = user_agent

        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def sanitize_filename(title: str) -> str:
        """
        Sanitizes a wiki title to be a valid filename.
        Replaces spaces with underscores and removes illegal characters.
        """
        # Remove namespace prefixes if present to keep filenames clean (optional)
        if ':' in title:
            safe_title = title.replace(':', '_')
        else:
            safe_title = title

        # Replace spaces and standard illegal filesystem chars
        safe_title = safe_title.strip().replace(' ', '_')
        # Regex removes: < > : " / \ | ? *
        safe_title = re.sub(r'[<>:"/\\|?*]', '', safe_title)

        # Truncate to avoid filesystem limits (usually 255 bytes)
        return safe_title[:200]

    def save_file(self, content: str, folder: Path, filename: str):
        """
        Writes the content to a .txt file in the specified folder.
        """
        filepath = folder / f"{filename}.txt"

        try:
            folder.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"Saved: {filepath}")
        except Exception as e:
            logger.error(f"Failed to write {filepath}: {e}")


class Crawler(MediaWikiTool):
    """
    Crawler implementation.
    Starts at a root page, parses links, and recursively downloads.
    """
    def __init__(self, base_url: str, output_dir: str, flat: bool, max_workers: int):
        super().__init__(output_dir)
        self.base_url = base_url
        self.flat_structure = flat
        self.max_workers = max_workers

        # Thread-safe set to keep track of visited pages to prevent cycles
        self.processed_pages: Set[str] = set()
        self.lock = threading.Lock()

    def get_wikitext_raw(self, page_title: str) -> Optional[str]:
        """
        Fetches raw wikitext using index.php?action=raw.
        """
        encoded_title = quote(page_title)
        # Construct URL. Assumes base_url points to index.php or script root
        if "index.php" in self.base_url:
            url = f"{self.base_url}?title={encoded_title}&action=raw"
        else:
            # Try to append index.php if not present
            base = self.base_url.rstrip('/')
            url = f"{base}/index.php?title={encoded_title}&action=raw"

        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.warning(f"Failed to fetch '{page_title}': {e}")
            return None

    def extract_links(self, wikitext: str) -> List[str]:
        """
        Finds internal MediaWiki links [[Link|Label]].
        """
        if not wikitext:
            return []

        # Regex to capture [[Link]] or [[Link|Text]]
        # It looks for pairs of brackets, capturing the content before any pipe |
        matches = re.findall(r'\[\[:?([^|\]]+)(?:\|[^\]]*)?\]\]', wikitext)

        unique_links = set()
        for match in matches:
            link = match.strip()
            # Ignore section links (#), external links (://), or empty strings
            if not link or link.startswith('#') or '://' in link:
                continue
            unique_links.add(link)
        return list(unique_links)

    def process_page(self, page_title: str, current_dir: Path) -> List[Tuple[str, Path]]:
        """
        Downloads a page and determines where its children should go.
        Returns a list of (child_title, child_directory) tuples.
        """
        # 1. Fetch Content
        wikitext = self.get_wikitext_raw(page_title)
        if not wikitext:
            return []

        # 2. Save Content
        sanitized_name = self.sanitize_filename(page_title)
        self.save_file(wikitext, current_dir, sanitized_name)

        # 3. Extract Links
        links = self.extract_links(wikitext)

        # 4. Determine directory for children
        # If flat structure is requested, children go to the same root output dir.
        # Otherwise, they go into a folder named after the CURRENT page.
        if self.flat_structure:
            next_dir = self.output_dir
        else:
            # Create a folder for this page's children: e.g. Parent/ChildFolder/
            next_dir = current_dir / sanitized_name

        return [(link, next_dir) for link in links]

    def run(self, start_page: str):
        """
        Main execution loop using a thread pool.
        """
        # Queue items are tuples: (page_title, parent_directory)
        queue = [(start_page, self.output_dir)]

        with self.lock:
            self.processed_pages.add(start_page)

        logger.info(f"Starting crawl from '{start_page}' with {self.max_workers} workers.")

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            while queue:
                # Snapshot current batch
                current_batch = queue[:]
                queue = []

                # Map futures to their metadata so we know which page caused an error
                future_to_meta = {}

                for page, folder in current_batch:
                    future = executor.submit(self.process_page, page, folder)
                    future_to_meta[future] = page

                # Process results as they complete
                for future in concurrent.futures.as_completed(future_to_meta):
                    page = future_to_meta[future]
                    try:
                        new_tasks = future.result() # Returns list of (child_link, child_folder)

                        with self.lock:
                            for child_link, child_folder in new_tasks:
                                # Only add to queue if we haven't processed it yet
                                if child_link not in self.processed_pages:
                                    self.processed_pages.add(child_link)
                                    queue.append((child_link, child_folder))

                    except Exception as e:
                        logger.error(f"Exception processing '{page}': {e}")

                if queue:
                    logger.info(f"Batch complete. Discovered {len(queue)} new unique links.")


class APIExporter(MediaWikiTool):
    """
    API Exporter implementation.
    Iterates over all pages using the 'allpages' API list.
    """
    def __init__(self, api_url: str, output_dir: str, namespace: Optional[int] = None):
        super().__init__(output_dir)
        self.api_url = api_url
        self.namespace = namespace

    def get_all_titles(self) -> List[str]:
        """
        Generator that yields all page titles from the API.
        """
        titles = []
        params = {
            "action": "query",
            "list": "allpages",
            "aplimit": "max",
            "format": "json"
        }
        if self.namespace is not None:
            params["apnamespace"] = self.namespace

        last_continue = {}

        while True:
            req_params = {**params, **last_continue}
            try:
                resp = self.session.get(self.api_url, params=req_params, timeout=30)
                resp.raise_for_status()
                data = resp.json()

                # Extract pages
                pages = data.get("query", {}).get("allpages", [])
                for p in pages:
                    titles.append(p["title"])

                # Check for continuation parameters
                if "continue" in data:
                    last_continue = data["continue"]
                else:
                    break
            except Exception as e:
                logger.error(f"API listing failed: {e}")
                break

        return titles

    def fetch_details(self, title: str) -> Tuple[Optional[str], List[str]]:
        """
        Fetches wikitext and categories for a specific title.
        """
        params = {
            "action": "query",
            "prop": "revisions|categories",
            "rvprop": "content",
            "cllimit": "max",
            "titles": title,
            "format": "json",
            "formatversion": "2"
        }

        try:
            resp = self.session.get(self.api_url, params=params, timeout=30)
            data = resp.json()

            # API returns a list of pages, we only asked for one
            page_list = data.get("query", {}).get("pages", [])
            if not page_list:
                return None, []

            page = page_list[0]
            if "missing" in page:
                return None, []

            # Extract content
            content = None
            revisions = page.get("revisions", [])
            if revisions:
                # Handle slots (newer MW versions) or direct content (older MW)
                rev = revisions[0]
                if "slots" in rev:
                    content = rev["slots"].get("main", {}).get("content")
                else:
                    content = rev.get("content")

            # Extract categories
            cats = []
            for c in page.get("categories", []):
                c_title = c.get("title", "")
                # Strip "Category:" prefix
                if ":" in c_title:
                    cats.append(c_title.split(":", 1)[1].strip())
                else:
                    cats.append(c_title)

            return content, cats

        except Exception as e:
            logger.error(f"Error fetching details for '{title}': {e}")
            return None, []

    def run(self):
        logger.info("Fetching page list via API...")
        titles = self.get_all_titles()
        logger.info(f"Found {len(titles)} pages. Starting download.")

        for i, title in enumerate(titles, 1):
            wikitext, categories = self.fetch_details(title)

            if wikitext:
                filename = self.sanitize_filename(title)

                # Determine folder based on first category (Topic)
                # If no category, put in root output folder
                if categories:
                    # Use the first category as the "Topic" folder
                    cat_folder = self.sanitize_filename(categories[0])
                    target_dir = self.output_dir / cat_folder
                else:
                    target_dir = self.output_dir

                self.save_file(wikitext, target_dir, filename)

                if i % 10 == 0:
                    logger.info(f"Processed {i}/{len(titles)} pages...")


def main():
    parser = argparse.ArgumentParser(description="Universal MediaWiki Downloader (API & Crawler) - Wikitext Only")

    # Mode selection
    parser.add_argument("--mode", choices=["api", "crawler"], default="crawler",
                        help="Operation mode. 'crawler' follows links recursively. 'api' lists all pages.")

    # Common arguments
    parser.add_argument("--url", required=True,
                        help="URL to wiki. For API mode: '.../api.php'. For Crawler: '.../index.php'")
    parser.add_argument("--output", default="wiki_dump", help="Output directory")

    # Crawler specific
    parser.add_argument("--start-page", default="Main_Page",
                        help="Entry point for the crawler (default: Main_Page)")
    parser.add_argument("--flat-output", action="store_true",
                        help="Disable recursive subfolders in crawler mode (puts everything in root)")
    parser.add_argument("--workers", type=int, default=5, help="Number of threads for crawler")

    # API specific
    parser.add_argument("--namespace", type=int, default=None,
                        help="API Mode: Limit to specific namespace (e.g. 0 for main)")

    args = parser.parse_args()

    print("------------------------------------------------")
    print(f"Mode:       {args.mode.upper()}")
    print(f"URL:        {args.url}")
    print(f"Output:     {args.output}")
    print("------------------------------------------------")

    if args.mode == "crawler":
        # Basic validation for crawler URL
        if "api.php" in args.url and "index.php" not in args.url:
            logger.warning("You passed an api.php URL to the crawler. It might fail. "
                           "Crawler usually expects index.php.")

        crawler = Crawler(
            base_url=args.url,
            output_dir=args.output,
            flat=args.flat_output,
            max_workers=args.workers
        )
        crawler.run(args.start_page)

    elif args.mode == "api":
        # Basic validation for API URL
        if "api.php" not in args.url:
             logger.warning("URL does not end in 'api.php'. API requests might fail.")

        exporter = APIExporter(
            api_url=args.url,
            output_dir=args.output,
            namespace=args.namespace
        )
        exporter.run()

if __name__ == "__main__":
    main()
