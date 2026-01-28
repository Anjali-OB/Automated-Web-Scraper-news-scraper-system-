from tasks.celery_app import celery_app
from scraper.selenium_scraper import get_bbc_page_source
from scraper.parser import parse_bbc_headlines
from database.db import insert_articles


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3, "countdown": 10})
def scrape_bbc_task(self):
    """
    Celery task to scrape BBC headlines and store them in DB.
    Retries automatically if something fails.
    """

    # 1️⃣ Fetch HTML using Selenium
    html = get_bbc_page_source()

    # 2️⃣ Parse headlines & URLs
    articles = parse_bbc_headlines(html)

    # 3️⃣ Store articles in database
    insert_articles(articles)

    return f"Stored {len(articles)} BBC articles"
