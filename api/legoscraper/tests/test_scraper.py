from django.test import TestCase

from ..scraper import LegoScraper

from selenium import webdriver

from decimal import Decimal

class ScraperTests(TestCase):
    """Tests for scraper module."""
    
    def setUp(self):
        self.scraper = LegoScraper()

    def test_get_page_count_correct(self):
        """Test get_page_count returns correct number of pages."""
        url = 'https://www.lego.com/pl-pl/themes/classic'
        page_count = self.scraper.get_page_count(url)

        self.assertEqual(page_count, 2)

    def test_scrape_themes_urls_success(self):
        """Test function returns list of themes urls correct."""
        urls = self.scraper.scrape_themes_urls('https://www.lego.com/pl-pl/themes')

        self.assertIn('https://www.lego.com/pl-pl/themes/classic', urls)

    def test_scrape_sets_urls_from_theme_success(self):
        """Test function returns list of sets urls correct."""
        urls = self.scraper.scrape_sets_urls_from_theme('https://www.lego.com/pl-pl/themes/classic')

        self.assertIn('https://www.lego.com/pl-pl/product/brick-separator-630', urls)

    def test_scrape_set_success(self):
        """Test scrape set function returns correct values."""
        url = 'https://www.lego.com/pl-pl/product/lego-creative-bricks-10692'
        fields = self.scraper.scrape_set(url)
        lego_set = {
            'title': 'Kreatywne klocki LEGO®',
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