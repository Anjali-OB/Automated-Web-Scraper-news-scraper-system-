from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_cnn(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []

    for tag in soup.select("h3.cd__headline"):
        title = tag.get_text(strip=True)
        parent = tag.find("a")
        url = urljoin("https://edition.cnn.com", parent["href"]) if parent else None

        articles.append({
            "title": title,
            "url": url,
            "source": "CNN"
        })

    return articles
