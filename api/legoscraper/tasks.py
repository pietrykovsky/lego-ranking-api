from celery import shared_task
from celery.utils.log import get_task_logger

from .scraper import LegoScraper

from .models import LegoSet

logger = get_task_logger(__name__)

@shared_task
def refresh_database():
    logger.info('Refreshing database...')