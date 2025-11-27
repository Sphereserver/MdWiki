#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MediaWiki Downloader & Crawler
=====================================================

This script merges the functionality of an API-based exporter and a recursive link crawler.

Key Features:
- Recursive folder structure for crawler (Parent/Child hierarchy).
- Multithreading for both API and Crawler modes.
- Connection pooling optimization.
- Configurable domain restriction.
- Downloads raw wikitext only.

Usage:
    # Crawler Mode: Default (follows all links)
    python3 mediawiki_merged.py --url "https://wiki.example.com/index.php" --mode crawler

    # Crawler Mode: Restrict to same domain (no external spam)
    python3 mediawiki_merged.py --url "https://wiki.example.com/index.php" --mode crawler --exclude-external

    # API Mode: Download all pages found via API
    python3 mediawiki_merged.py --url "https://wiki.example.com/api.php" --mode api
"""

import argparse
import concurrent.futures
import logging
import re
import threading
from pathlib import Path
from typing import List, Optional, Set, Tuple
from urllib.parse import quote, urlparse

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

class MediaWikiTool:
    """
    Base class containing shared utilities.
    """
    def __init__(self, output_dir: str, workers: int, user_agent: str = "MediaWikiDownloader/2.2"):
        self.output_dir = Path(output_dir)
        self.workers = workers
        self.user_agent = user_agent

        self.session = requests.Session()
        self.session.headers["User-Agent"] = user_agent

        # Configure retry strategy and connection pool
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        # pool_maxsize must be >= workers to avoid "Connection pool is full" warning
        adapter = HTTPAdapter(pool_connections=workers, pool_maxsize=workers, max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        self.output_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def sanitize_filename(title: str) -> str:
        if ':' in title:
            safe_title = title.replace(':', '_')
        else:
            safe_title = title
        safe_title = safe_title.strip().replace(' ', '_')
        safe_title = re.sub(r'[<>:"/\\|?*]', '', safe_title)
        return safe_title[:200]

    def save_file(self, content: str, folder: Path, filename: str) -> Path:
        filepath = folder / f"{filename}.txt"
        try:
            folder.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return filepath
        except Exception as e:
            logger.error(f"Failed to write {filepath}: {e}")
            return filepath


class Crawler(MediaWikiTool):
    """
    Crawler implementation using ThreadPoolExecutor.
    """
    def __init__(self, base_url: str, output_dir: str, flat: bool, workers: int, exclude_external: bool):
        super().__init__(output_dir, workers)
        self.base_url = base_url
        self.flat_structure = flat
        self.exclude_external = exclude_external

        # Parse the base domain to filter external links if requested
        parsed_url = urlparse(base_url)
        self.allowed_domain = parsed_url.netloc

        self.processed_pages: Set[str] = set()
        self.lock = threading.Lock()

    def is_external_link(self, link: str) -> bool:
        """
        Checks if a link is external (different domain).
        """
        if '://' in link:
            parsed = urlparse(link)
            # If the domain is different from the base URL, it's external
            if parsed.netloc and parsed.netloc != self.allowed_domain:
                return True
        return False

    def get_wikitext_raw(self, page_title: str) -> Optional[str]:
        encoded_title = quote(page_title)
        if "index.php" in self.base_url:
            url = f"{self.base_url}?title={encoded_title}&action=raw"
        else:
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
        if not wikitext: return []

        matches = re.findall(r'\[\[:?([^|\]]+)(?:\|[^\]]*)?\]\]', wikitext)
        unique_links = set()
        for match in matches:
            link = match.strip()

            if not link or link.startswith('#'):
                continue

            # If user requested to exclude external links, check the domain
            if self.exclude_external and self.is_external_link(link):
                continue

            # Note: This regex captures [[...]]. Standard MediaWiki external links use [...].
            # However, some wikis use [[http://...](http://...)] or interwiki links.
            # If you are getting spam via standard external links like [http://...](http://...),
            # you would need a second regex, but standard crawler logic usually follows internal pages only.
            # This script currently only follows [[...]] links.
            # If 'spam' pages are being reached, they must be linked via [[...]].

            unique_links.add(link)
        return list(unique_links)

    def process_page(self, page_title: str, current_dir: Path) -> List[Tuple[str, Path]]:
        # 1. Fetch
        wikitext = self.get_wikitext_raw(page_title)
        if not wikitext:
            return []

        # 2. Save
        sanitized_name = self.sanitize_filename(page_title)
        saved_path = self.save_file(wikitext, current_dir, sanitized_name)

        # Log the full relative path so user can see folder structure
        try:
            rel_path = saved_path.relative_to(self.output_dir)
            logger.info(f"[Crawler] Saved: {rel_path}")
        except ValueError:
            # Fallback if path issues occur
            logger.info(f"[Crawler] Saved: {saved_path}")

        # 3. Parse Links
        links = self.extract_links(wikitext)

        # 4. Determine Next Dir
        if self.flat_structure:
            next_dir = self.output_dir
        else:
            next_dir = current_dir / sanitized_name

        return [(link, next_dir) for link in links]

    def run(self, start_page: str):
        queue = [(start_page, self.output_dir)]

        with self.lock:
            self.processed_pages.add(start_page)

        domain_msg = f" (Restricted to {self.allowed_domain})" if self.exclude_external else ""
        logger.info(f"Starting crawl from '{start_page}'{domain_msg}")

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.workers) as executor:
            while queue:
                current_batch = queue[:]
                queue = []

                future_to_page = {}
                for page, folder in current_batch:
                    future = executor.submit(self.process_page, page, folder)
                    future_to_page[future] = page

                for future in concurrent.futures.as_completed(future_to_page):
                    page = future_to_page[future]
                    try:
                        new_tasks = future.result()
                        with self.lock:
                            for child_link, child_folder in new_tasks:
                                if child_link not in self.processed_pages:
                                    self.processed_pages.add(child_link)
                                    queue.append((child_link, child_folder))
                    except Exception as e:
                        logger.error(f"Exception processing '{page}': {e}")

                if queue:
                    logger.info(f"Batch complete. {len(queue)} new links queued.")


class APIExporter(MediaWikiTool):
    """
    API Exporter implementation using ThreadPoolExecutor.
    """
    def __init__(self, api_url: str, output_dir: str, workers: int, namespace: Optional[int] = None):
        super().__init__(output_dir, workers)
        self.api_url = api_url
        self.namespace = namespace

    def get_all_titles(self) -> List[str]:
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

        logger.info("Fetching full page list from API...")
        while True:
            req_params = {**params, **last_continue}
            try:
                resp = self.session.get(self.api_url, params=req_params, timeout=30)
                resp.raise_for_status()
                data = resp.json()

                pages = data.get("query", {}).get("allpages", [])
                for p in pages:
                    titles.append(p["title"])

                if "continue" in data:
                    last_continue = data["continue"]
                else:
                    break
            except Exception as e:
                logger.error(f"API listing failed: {e}")
                break
        return titles

    def fetch_and_save(self, title: str):
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
            page_list = data.get("query", {}).get("pages", [])

            if not page_list: return
            page = page_list[0]
            if "missing" in page: return

            content = None
            revisions = page.get("revisions", [])
            if revisions:
                rev = revisions[0]
                if "slots" in rev:
                    content = rev["slots"].get("main", {}).get("content")
                else:
                    content = rev.get("content")

            if content:
                cats = []
                for c in page.get("categories", []):
                    c_title = c.get("title", "")
                    if ":" in c_title:
                        cats.append(c_title.split(":", 1)[1].strip())
                    else:
                        cats.append(c_title)

                filename = self.sanitize_filename(title)
                if cats:
                    cat_folder = self.sanitize_filename(cats[0])
                    target_dir = self.output_dir / cat_folder
                else:
                    target_dir = self.output_dir

                saved_path = self.save_file(content, target_dir, filename)
                try:
                    rel_path = saved_path.relative_to(self.output_dir)
                    # logger.info(f"[API] Saved: {rel_path}")
                    # Commented out to reduce API spam log, uncomment if desired
                except:
                    pass

        except Exception as e:
            logger.error(f"Error processing '{title}': {e}")

    def run(self):
        titles = self.get_all_titles()
        total = len(titles)
        logger.info(f"Found {total} pages. Starting threaded download with {self.workers} workers.")

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = {executor.submit(self.fetch_and_save, title): title for title in titles}

            completed = 0
            for _ in concurrent.futures.as_completed(futures):
                completed += 1
                if completed % 50 == 0:
                    logger.info(f"Progress: {completed}/{total}")


def main():
    parser = argparse.ArgumentParser(description="Universal MediaWiki Downloader")

    parser.add_argument("--mode", choices=["api", "crawler"], default="crawler",
                        help="Operation mode.")
    parser.add_argument("--url", required=True,
                        help="URL to wiki.")
    parser.add_argument("--output", default="wiki_dump", help="Output directory")
    parser.add_argument("--workers", type=int, default=10,
                        help="Number of parallel threads (default: 10)")

    # Crawler specific
    parser.add_argument("--start-page", default="Main_Page",
                        help="Crawler entry point")
    parser.add_argument("--flat-output", action="store_true",
                        help="Disable subfolders in crawler mode")
    parser.add_argument("--exclude-external", action="store_true",
                        help="Do not follow links to different domains (default: follow everything)")

    # API specific
    parser.add_argument("--namespace", type=int, default=None,
                        help="Limit to specific namespace (API mode only)")

    args = parser.parse_args()

    print(f"--- MediaWiki Downloader ---")
    print(f"Mode:    {args.mode.upper()}")
    print(f"URL:     {args.url}")
    print(f"Workers: {args.workers}")
    print(f"Output:  {args.output}")
    print(f"Exclude External: {args.exclude_external}")
    print(f"----------------------------")

    if args.mode == "crawler":
        if "api.php" in args.url and "index.php" not in args.url:
            logger.warning("Warning: api.php URL passed to crawler. Expects index.php usually.")

        crawler = Crawler(
            base_url=args.url,
            output_dir=args.output,
            flat=args.flat_output,
            workers=args.workers,
            exclude_external=args.exclude_external
        )
        crawler.run(args.start_page)

    elif args.mode == "api":
        if "api.php" not in args.url:
             logger.warning("Warning: URL does not end in 'api.php'.")

        exporter = APIExporter(
            api_url=args.url,
            output_dir=args.output,
            workers=args.workers,
            namespace=args.namespace
        )
        exporter.run()

if __name__ == "__main__":
    main()
