from django.test import TestCase

from ..tasks import refresh_database

from ..models import LegoSet
from ..scraper import LegoScraper

def availability_string_to_bool(available):
    """Convert availability to boolean value."""
    if available == 'Dostępne teraz':
        return True

    return False

class TasksTests(TestCase):
    """Test celery tasks."""

    def test_refresh_database_success(self):
        """Test refresh_database fills the database with legosets."""
        url = 'https://www.lego.com/pl-pl/themes'
        scraper = LegoScraper(url)
        scraped_sets = scraper.scrape()
        refresh_database()
        legosets = LegoSet.objects.all()
        for set in scraped_sets:
            legoset = legosets.get(product_id=set['product_id'])
            self.assertIsNotNone(legoset)
            set['available'] = availability_string_to_bool(set['available'])
            for k in set:
                if k == 'theme' and k == 'age':
                    self.assertEqual(legoset[k].name, set[k])
                else:    
                    self.assertEqual(legoset[k], set[k])