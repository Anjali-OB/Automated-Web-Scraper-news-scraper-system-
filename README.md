#  Automated Web Scraper System

A scalable news scraping system that collects data from dynamic websites using Selenium, processes it using Celery background workers, and stores structured data in a database.

##  Features
- Dynamic website scraping (Selenium)
- Multi-source support (BBC, CNN, Reuters)
- Background task processing (Celery)
- Scheduled jobs (Celery Beat)
- Database storage
- Modular & scalable architecture

##  Tech Stack
- Python
- Selenium
- Celery
- Redis
- BeautifulSoup
- SQLite / PostgreSQL

##  How to Run
```bash
redis-server
celery -A news_scraper.tasks.celery_app worker -l info
celery -A news_scraper.tasks.celery_app beat -l info
