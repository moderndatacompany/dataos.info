import logging
import time
from collections import deque
from urllib.parse import urlparse, urljoin, urlunparse

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# --------------------------
# Logging
# --------------------------
logging.basicConfig(
    filename='link_checker.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# --------------------------
# URL helpers
# --------------------------
def is_valid_url(url: str) -> bool:
    p = urlparse(url)
    return p.scheme in ("http", "https") and bool(p.netloc)

def normalize_url(url: str) -> str:
    """
    Normalize URL:
    - lowercase scheme/host
    - drop fragment
    - keep query/params
    - ensure path is at least '/'
    """
    p = urlparse(url)
    p = p._replace(
        scheme=p.scheme.lower(),
        netloc=p.netloc.lower(),
        fragment=""
    )
    path = p.path or "/"
    p = p._replace(path=path)
    return urlunparse(p)

def same_site(href: str, start_host: str) -> bool:
    """
    True if href is on the same host or a subdomain of start_host.
    """
    host = urlparse(href).netloc.lower()
    start_host = start_host.lower()
    return host == start_host or host.endswith("." + start_host)

# --------------------------
# HTML helpers
# --------------------------
def get_nearest_heading(soup: BeautifulSoup, element) -> str:
    for previous in element.find_all_previous(['h1','h2','h3','h4','h5','h6']):
        return previous.get_text(strip=True)
    return "No heading found"

# --------------------------
# Networking
# --------------------------
def build_session() -> requests.Session:
    s = requests.Session()
    s.headers["User-Agent"] = "link-checker"
    retry = Retry(
        total=4,
        connect=4,
        read=4,
        status=4,
        backoff_factor=0.6,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=50, pool_maxsize=50)
    s.mount("http://", adapter)
    s.mount("https://", adapter)
    return s

# --------------------------
# Crawler
# --------------------------
def crawl_and_check(start_url: str, max_pages: int = 100000, max_depth: int = 50, delay: float = 0.10):
    """
    Broad, thorough same-site crawl:
    - Checks ALL links (records status for any content-type)
    - Crawls only HTML pages deeper
    """
    session = build_session()

    start_url = normalize_url(start_url)
    start_host = urlparse(start_url).netloc

    # visited holds normalized URLs we've already fetched
    visited = set([start_url])

    # queue items: (url, depth, link_text, parent_url, heading_text)
    queue = deque([(start_url, 0, None, None, None)])

    while queue and len(visited) <= max_pages:
        url, depth, link_text, parent, heading_text = queue.popleft()
        try:
            resp = session.get(url, timeout=30, allow_redirects=True)
            final_url = normalize_url(resp.url)
            status = resp.status_code
            ctype = resp.headers.get("Content-Type", "")

            # Pass/Fail logging for this fetched URL
            if status == 200:
                logging.info(
                    f"[PASS] {final_url} ({ctype}) - Link text: \"{link_text}\" "
                    f"Near heading: \"{heading_text}\" Found on: {parent} "
                    f"Time: {resp.elapsed.total_seconds():.2f}s"
                )
            else:
                logging.warning(
                    f"[FAIL] {final_url} - Status {status} - Link text: \"{link_text}\" "
                    f"Near heading: \"{heading_text}\" Found on: {parent}"
                )

            # Crawl deeper only if page is HTML and depth allows
            if "text/html" in ctype.lower() and depth < max_depth:
                soup = BeautifulSoup(resp.text, "html.parser")

                # Extract and check every <a href>, enqueue HTML pages
                for a_tag in soup.find_all("a", href=True):
                    raw_href = a_tag["href"].strip()

                    # Skip obvious non-navigational schemes / in-page anchors
                    if raw_href.startswith(("#", "javascript:", "data:", "mailto:", "tel:")):
                        continue

                    abs_href = urljoin(final_url, raw_href)
                    norm = normalize_url(abs_href)
                    if not is_valid_url(norm):
                        continue

                    # Only check links belonging to the same site
                    if not same_site(norm, start_host):
                        continue

                    # If we haven't fetched it yet, decide whether to crawl or just check
                    if norm not in visited:
                        # We'll *always* record the status when we fetch it.
                        visited.add(norm)

                        # For logging context
                        link_text = a_tag.get_text(strip=True)
                        near_heading = get_nearest_heading(soup, a_tag)

                        # Enqueue; the fetch will both check and (if HTML) crawl
                        queue.append((norm, depth + 1, link_text, final_url, near_heading))

            time.sleep(delay)

        except requests.RequestException as e:
            logging.error(
                f"[ERROR] {url} - {e} - Link text: \"{link_text}\" "
                f"Near heading: \"{heading_text}\" Found on: {parent}",
                exc_info=False
            )

# --------------------------
# Entry
# --------------------------
if __name__ == "__main__":
    # Use HTTPS canonical start; widen coverage by allowing deep depth/page count.
    start_url = "https://dataos.info/"
    crawl_and_check(start_url)



# process to execute

    # change the directory 
    # - activate the virtual environment - source myenv/bin/activate
    # - install the requirements if not downloaded already:  pip install -r requirements.txt
    # - python3 link_checker.py