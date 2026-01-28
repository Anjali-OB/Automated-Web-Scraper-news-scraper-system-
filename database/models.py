"""
models.py

This file handles:
- Inserting news articles into the database
- Fetching stored news articles
"""

from database.db import get_db_connection


def insert_news_articles(articles):
    """
    Insert a list of news articles into the database.

    Args:
        articles (list): List of dictionaries with news data
    """

    conn = get_db_connection()
    cursor = conn.cursor()

    for article in articles:
        try:
            # Insert article into database
            cursor.execute("""
                INSERT INTO news_articles (headline, url, source)
                VALUES (?, ?, ?)
            """, (
                article["headline"],
                article["url"],
                article["source"]
            ))

        except Exception:
            # Ignore duplicate entries (same URL)
            continue

    # Commit all inserts at once
    conn.commit()
    conn.close()


def fetch_all_articles():
    """
    Fetch all stored news articles from database.

    Returns:
        list: List of stored articles
    """

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM news_articles")
    rows = cursor.fetchall()

    conn.close()

    return rows
