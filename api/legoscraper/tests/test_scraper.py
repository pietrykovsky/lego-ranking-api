from django.test import TestCase

from ..scraper import LegoScraper

from decimal import Decimal

class ScraperTests(TestCase):
    """Tests for scraper module."""
    
    def setUp(self):
        themes_url = 'https://www.lego.com/pl-pl/themes/'
        self.scraper = LegoScraper(themes_url)

    def test_get_pages_count_correct(self):
        """Test get_pages_count returns correct number of pages."""
        url = 'https://www.lego.com/pl-pl/themes/classic'
        pages_count = self.scraper.get_pages_count(url)

        self.assertEqual(pages_count, 2)

    def test_scrape_themes_urls_success(self):
        """Test function returns list of themes urls correct."""
        urls = self.scraper.scrape_themes_urls()

        self.assertIn('https://www.lego.com/pl-pl/themes/speed-champions', urls)

    def test_scrape_sets_urls_from_theme_success(self):
        """Test function returns list of sets urls correct."""
        urls = self.scraper.scrape_sets_urls_from_theme('https://www.lego.com/pl-pl/themes/technic')

        self.assertIn('https://www.lego.com/pl-pl/product/ferrari-daytona-sp3-42143', urls)

    def test_scrape_set_success(self):
        """Test scrape set function returns correct values."""
        url = 'https://www.lego.com/pl-pl/product/lego-creative-bricks-10692'
        fields = self.scraper.scrape_set(url)
        lego_set = {
            'title': 'Kreatywne klocki LEGO® 10692',
            'product_id': '10692',
            'theme': 'Classic',
            'price': Decimal("69.99"),
            'available': 'Dostępne teraz',
            'age': '4-99',
            'elements': 221,
            'link': url,
            'minifigures': None,
        }
        for k, v in lego_set.items():
            self.assertEqual(fields[k], v)

    def test_scrape_legostore_success(self):
        """Test scrape whole lego store from lego sets success."""
        lego_sets = self.scraper.scrape()
        for lego_set in lego_sets:
            del lego_set['minifigures']
            for k in lego_set:
                self.assertIsNotNone(lego_set[k])
        self.assertIsNotNone(lego_sets)