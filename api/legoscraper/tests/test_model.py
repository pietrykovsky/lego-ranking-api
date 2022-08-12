from django.test import TestCase

from decimal import Decimal

from ..models import LegoSet

class ModelTests(TestCase):
    """Tests for legoscraper models."""

    def test_create_legoset_success(self):
        """Test create legoset object."""
        fields = {
            'title': 'test title',
            'product_id': '10283',
            'theme': 'lego-icons',
            'price': Decimal('849.99'),
            'available': True,
            'age': '18+',
            'elements': 2354,
            'link': 'https://www.lego.com/pl-pl/product/nasa-space-shuttle-discovery-10283',
        }
        legoset = LegoSet.objects.create(**fields)

        for k, v in fields.items():
            self.assertEqual(getattr(legoset, k), v)
        self.assertEqual(legoset.minifigures, None)

    def test_legoset_price_per_element_correct(self):
        """Test price per element property returns a correct value."""
        fields = {
            'title': 'test title',
            'product_id': '10283',
            'theme': 'lego-icons',
            'price': Decimal('333.33'),
            'available': True,
            'age': '18+',
            'elements': 2,
            'link': 'https://www.lego.com/pl-pl/product/nasa-space-shuttle-discovery-10283',
        }
        legoset = LegoSet.objects.create(**fields)

        self.assertEqual(legoset.price_per_element, Decimal('166.66'))