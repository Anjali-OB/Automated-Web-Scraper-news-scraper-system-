from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_bbc(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []

    for tag in soup.find_all("h2"):
        title = tag.get_text(strip=True)
        if len(title) < 20:
            continue

        parent = tag.find_parent("a")
        url = urljoin("https://www.bbc.com", parent["href"]) if parent else None

        articles.append({
            "title": title,
            "url": url,
            "source": "BBC"
        })

    return articles
