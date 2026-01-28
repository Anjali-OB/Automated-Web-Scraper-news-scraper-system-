from news_scraper.tasks.celery_app import celery_app
from news_scraper.utils.logger import logger


SITES = {
    "bbc": {
        "url": "https://www.bbc.com/news",
        "parser": "news_scraper.scraper.bbc.scrape_bbc",
    },
    "cnn": {
        "url": "https://edition.cnn.com",
        "parser": "news_scraper.scraper.cnn.scrape_cnn",
    },
    "reuters": {
        "url": "https://www.reuters.com",
        "parser": "news_scraper.scraper.reuters.scrape_reuters",
    },
}


@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 3, "countdown": 30},
    retry_backoff=True,
    name="news_scraper.tasks.scraper_tasks.scrape_site",
)
def scrape_site(self, site_name):
    try:
        logger.info(f"Scraping started for {site_name}")

        from importlib import import_module
        from news_scraper.scraper.selenium_scraper import get_page_source
        from news_scraper.database.db import insert_articles

        site = SITES[site_name]
        html = get_page_source(site["url"])

        module_path, func_name = site["parser"].rsplit(".", 1)
        parser_func = getattr(import_module(module_path), func_name)

        articles = parser_func(html)
        insert_articles(articles)

        logger.info(f"{site_name}: Inserted {len(articles)} articles")
        return len(articles)

    except Exception as e:
        logger.error(f"{site_name} failed: {e}", exc_info=True)
        raise self.retry(exc=e)
