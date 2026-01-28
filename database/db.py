import sqlite3

DB_PATH = "news_scraper/database/news.db"


def insert_articles(articles):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            headline TEXT,
            url TEXT,
            source TEXT
        )
    """)

    for article in articles:
        cursor.execute(
            "INSERT INTO news (headline, url, source) VALUES (?, ?, ?)",
            (article["headline"], article["url"], article["source"])
        )

    conn.commit()
    conn.close()
