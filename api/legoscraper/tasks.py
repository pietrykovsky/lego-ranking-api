from celery import shared_task
from celery.utils.log import get_task_logger

from .scraper import LegoScraper

from .models import LegoSet

logger = get_task_logger(__name__)

@shared_task
def refresh_database():
    """Scrape data from lego store and add it to the database."""
    logger.info('Refreshing database...')
    
    themes_url = 'https://www.lego.com/pl-pl/themes'
    scraper = LegoScraper(themes_url)
    scraped_sets = scraper.scrape()
    for scraped_data in scraped_sets:
        lego_set, created = LegoSet.objects.update_or_create(product_id=scraped_data['product_id'], defaults=scraped_data)
        if created:
            logger.info(f'{lego_set} has been updated.')
        else:
            logger.info(f'{lego_set} has been added to database.')

    logger.info('Refreshing database complete.')