import csv
import os
from datetime import datetime

def export_articles_to_csv(articles):
    if not articles:
        return

    os.makedirs("exports", exist_ok=True)

    filename = f"exports/bbc_news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["headline", "url", "source"]
        )
        writer.writeheader()
        writer.writerows(articles)

    print(f"CSV exported: {filename}")
