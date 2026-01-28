from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_reuters(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []

    for tag in soup.select("a[data-testid='Heading']"):
        title = tag.get_text(strip=True)
        url = urljoin("https://www.reuters.com", tag["href"])

        articles.append({
            "title": title,
            "url": url,
            "source": "Reuters"
        })

    return articles
