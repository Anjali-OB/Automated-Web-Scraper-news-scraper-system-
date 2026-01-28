from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "news_scraper",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

celery_app.autodiscover_tasks(["news_scraper.tasks"])

celery_app.conf.beat_schedule = {
    "bbc-every-10-min": {
        "task": "news_scraper.tasks.scraper_tasks.scrape_site",
        "schedule": crontab(minute="*/10"),
        "args": ("bbc",),
    },
    "cnn-every-15-min": {
        "task": "news_scraper.tasks.scraper_tasks.scrape_site",
        "schedule": crontab(minute="*/15"),
        "args": ("cnn",),
    },
    "reuters-every-30-min": {
        "task": "news_scraper.tasks.scraper_tasks.scrape_site",
        "schedule": crontab(minute="*/30"),
        "args": ("reuters",),
    },
}
