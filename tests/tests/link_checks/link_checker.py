import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import logging

# Configure logging to record the status of link checks.
logging.basicConfig(
    filename='link_checker.log',  # Log file name.
    level=logging.INFO,  # Logging level.
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log record format.
    datefmt='%Y-%m-%d %H:%M:%S'  # Timestamp format.
)

visited_urls = set()  # A set to keep track of visited URLs to avoid re-checking.

def is_valid_url(url):
    """
    Validates a given URL.
    
    Parameters:
        url (str): The URL to validate.
    
    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_nearest_heading(soup, element):
    """
    Finds the nearest heading to a specified element within an HTML document.
    
    Parameters:
        soup (BeautifulSoup): The BeautifulSoup object of the HTML document.
        element (Tag): The BeautifulSoup Tag object to find the nearest heading for.
    
    Returns:
        str: The text of the nearest heading or a default string if no heading is found.
    """
    for previous in element.find_all_previous(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        return previous.text.strip()
    return "No heading found"

def get_all_website_links(url, domain_name):
    """
    Retrieves all URLs that are found on `url` in which it belongs to the same website.
    
    Parameters:
        url (str): The URL of the webpage to scan for links.
        domain_name (str): The domain name of the website to limit the search to.
    
    Returns:
        set: A set of tuples containing the link URL, link text, nearest heading, and page URL.
    """
    urls = set()
    global visited_urls
    if url in visited_urls:
        return urls
    visited_urls.add(url)
    try:
        session = requests.Session()
        session.headers["User-Agent"] = "link-checker"
        response = session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                continue
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not is_valid_url(href) or href in urls or domain_name not in href:
                continue
            heading = get_nearest_heading(soup, a_tag)
            urls.add((href, a_tag.text.strip(), heading, url))  # Include context information
    except requests.RequestException as e:
        logging.error(f"Failed to get links from {url}: {e}")
    return urls

def check_link(url, link_text, heading, page_url):
    """
    Checks a single link for validity and logs the outcome.
    
    Parameters:
        url (str): The URL of the link to check.
        link_text (str): The text of the link.
        heading (str): The nearest heading to the link in the HTML document.
        page_url (str): The URL of the page where the link was found.
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            logging.info(f"[PASS] {url} - Link text: \"{link_text}\", Near heading: \"{heading}\", Found on: {page_url}")
        else:
            logging.warning(f"[FAIL] {url} - Status Code: {response.status_code} - Link text: \"{link_text}\", Near heading: \"{heading}\", Found on: {page_url}")
    except requests.RequestException as e:
        logging.error(f"[ERROR] {url} - {e} - Link text: \"{link_text}\", Near heading: \"{heading}\", Found on: {page_url}")

def crawl_and_check(url):
    """
    Recursively crawls a webpage and checks all links found on it.
    
    Parameters:
        url (str): The URL of the webpage to start crawling from.
    """
    global visited_urls
    domain_name = urlparse(url).netloc
    all_links = get_all_website_links(url, domain_name)
    for link, link_text, heading, page_url in all_links:
        if link not in visited_urls:
            check_link(link, link_text, heading, page_url)
            crawl_and_check(link)  # Recursive call to check links found on this page

if __name__ == "__main__":
    start_url = "http://localhost:8000/"  # The initial URL to begin crawling from.
    crawl_and_check(start_url)


    # process to execute
# change the diretory 
# - activate the virtual environment - source myenv/bin/activate
# - install the requirements if not downloaded already:  pip install -r requirements.txt
# - python3 link_checker.py