from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

def get_broken_links(url=None):
    # Set root domain.
    root_domain = "veganmsp.com"
    if url is None:
        url = f"https://{root_domain}"

    # Internal function for validating HTTP status code.
    def _validate_url(url):
        if url.startswith('/'):
            url = f'https://{root_domain}{url}'
        r = requests.head(url)
        if r.status_code == 404:
            broken_links.append(url)

    # Make request to URL.
    data = requests.get(url).text

    # Parse HTML from request.
    soup = BeautifulSoup(data, features="html.parser")

    # Create a list containing all links with the root domain.
    links = [link.get("href") for link in soup.find_all("a")]

    broken_links = []

    # Loop through links checking for 404 responses, and append to list.
    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(_validate_url, links)

    return broken_links

if __name__ == '__main__':
    _broken_links = get_broken_links()
    print(_broken_links)
    for _link in _broken_links:
        print(_link)
