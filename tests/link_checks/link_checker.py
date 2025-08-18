import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urlunparse
import logging
from collections import deque
import time

# Configure logging to record the status of link checks.
logging.basicConfig(
    filename='link_checker.log',  # Log file name.
    level=logging.INFO,  # Logging level.
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log record format.
    datefmt='%Y-%m-%d %H:%M:%S'  # Timestamp format.
)

def is_valid_url(url):
    """
    Validates a given URL.
    """
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)

def normalize_url(url):
    """
    Normalize URL: lowercase scheme/host, drop fragments, keep query.
    """
    parsed = urlparse(url)
    parsed = parsed._replace(
        scheme=parsed.scheme.lower(),
        netloc=parsed.netloc.lower(),
        fragment=""
    )
    return urlunparse(parsed)

def same_site(href, start_host):
    """
    Check whether href belongs to the same site as start_host.
    """
    host = urlparse(href).netloc.lower()
    start_host = start_host.lower()
    return host == start_host or host.endswith("." + start_host)

def get_nearest_heading(soup, element):
    """
    Finds the nearest heading to a specified element within an HTML document.
    """
    for previous in element.find_all_previous(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        return previous.text.strip()
    return "No heading found"

def crawl_and_check(start_url, max_pages=1000, max_depth=5, delay=0.2):
    """
    Iteratively crawls a website and checks links.
    """
    session = requests.Session()
    session.headers["User-Agent"] = "link-checker"

    start_url = normalize_url(start_url)
    start_host = urlparse(start_url).netloc

    visited = set([start_url])
    queue = deque([(start_url, 0, None, None)])  # (url, depth, link_text, parent_url)

    while queue and len(visited) <= max_pages:
        url, depth, link_text, parent = queue.popleft()

        try:
            response = session.get(url, timeout=15, allow_redirects=True)
            final_url = normalize_url(response.url)
            status = response.status_code
            ctype = response.headers.get("Content-Type", "")

            if status == 200:
                logging.info(
                    f"[PASS] {final_url} ({ctype}) - Link text: \"{link_text}\" "
                    f"Found on: {parent} - {response.elapsed.total_seconds():.2f}s"
                )
            else:
                logging.warning(
                    f"[FAIL] {final_url} - Status {status} - Link text: \"{link_text}\" "
                    f"Found on: {parent}"
                )

            # Crawl only HTML pages and within depth
            if "text/html" in ctype and depth < max_depth:
                soup = BeautifulSoup(response.text, "html.parser")
                for a_tag in soup.find_all("a", href=True):
                    href_abs = urljoin(final_url, a_tag["href"])
                    norm = normalize_url(href_abs)
                    if not is_valid_url(norm):
                        continue
                    if not same_site(norm, start_host):
                        continue
                    if norm not in visited:
                        visited.add(norm)
                        heading = get_nearest_heading(soup, a_tag)
                        queue.append((norm, depth + 1, a_tag.get_text(strip=True), final_url))
            time.sleep(delay)
        except requests.RequestException as e:
            logging.error(
                f"[ERROR] {url} - {e} - Link text: \"{link_text}\" Found on: {parent}",
                exc_info=False
            )

if __name__ == "__main__":
    start_url = "http://localhost:8000/"  # The initial URL to begin crawling from.
    crawl_and_check(start_url)

    
# process to execute

    # change the diretory 
    # - activate the virtual environment - source myenv/bin/activate
    # - install the requirements if not downloaded already:  pip install -r requirements.txt
    # - python3 link_checker.py