"""
parser.py

This file is responsible for:
- Parsing HTML using BeautifulSoup
- Extracting news headlines, links, and categories
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin


def parse_bbc_news(html):
    """
    Parse BBC News HTML and extract headlines.

    Args:
        html (str): HTML content of BBC News page

    Returns:
        list: List of dictionaries containing news data
    """

    soup = BeautifulSoup(html, "html.parser")
    articles = []

    # Find all headline tags (BBC uses h2 heavily)
    headline_tags = soup.find_all("h2")

    for tag in headline_tags:
        headline_text = tag.get_text(strip=True)

        # Skip empty or very short headlines
        if not headline_text or len(headline_text) < 20:
            continue

        # Try to find parent anchor tag
        parent_link = tag.find_parent("a")

        if parent_link and parent_link.get("href"):
            article_url = urljoin("https://www.bbc.com", parent_link["href"])
        else:
            article_url = None

        article = {
            "headline": headline_text,
            "url": article_url,
            "source": "BBC",
        }

        articles.append(article)

    return articles
