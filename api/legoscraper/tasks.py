from celery import shared_task
from celery.utils.log import get_task_logger

from .scraper import LegoScraper

from .models import LegoSet

logger = get_task_logger(__name__)

@shared_task
def refresh_database():
    logger.info('Refreshing database...')
    
    scraper = LegoScraper()
    themes_url = 'https://www.lego.com/pl-pl/themes'
    themes_urls = scraper.scrape_themes_urls(themes_url)

    for theme_url in themes_urls:
        sets_urls = scraper.scrape_sets_urls_from_theme(theme_url)

        for set_url in sets_urls:
            scraped_data = scraper.scrape_set(set_url) 
            lego_set, created = LegoSet.objects.get_or_create(product_id=scraped_data['product_id'])

            if not created:
                for attr, value in scraped_data.items():
                    setattr(lego_set, attr, value)
                lego_set.save()

    logger.info('Refreshing database complete.')