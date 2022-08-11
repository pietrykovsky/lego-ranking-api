from django.test import TestCase

from decimal import Decimal

from .models import LegoSet

class ModelTests(TestCase):
    """Tests for legoscraper models."""
# name of set, price, theme, elements, product id, photo, available, age, minifigures, link
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
            'minifigures': None,
        }
        legoset = LegoSet.objects.create(fields['title'], fields['product_id'], fields['theme'], fields['price'], fields['available'], fields['age'], fields['elements'], fields['link'], fields['minifigures'])

        for k, v in fields.items():
            self.assertEqual(getattr(legoset, k), v)


