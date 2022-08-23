from django.test import TestCase

from decimal import Decimal

from ..models import LegoSet, Theme, AgeCategory

class ModelTests(TestCase):
    """Tests for legoscraper models."""

    def test_create_theme_success(self):
        """Test create theme object is successful."""
        name = 'Classic'
        theme = Theme.objects.create(name=name)

        self.assertEqual(theme.name, name)

    def test_create_age_category_success(self):
        """Test create age category object is successful."""
        name = '18+'
        age_category = AgeCategory.objects.create(name=name)

        self.assertEqual(age_category.name, name)
            
    def test_create_legoset_success(self):
        """Test create legoset object."""
        theme = Theme.objects.create(name='Classic')
        age_category = AgeCategory.objects.create(name='18+')
        fields = {
            'title': 'test title',
            'product_id': '10283',
            'theme': theme,
            'price': Decimal('849.99'),
            'available': True,
            'age': age_category,
            'elements': 2354,
            'link': 'https://www.lego.com/pl-pl/product/nasa-space-shuttle-discovery-10283',
        }
        legoset = LegoSet.objects.create(**fields)

        for k, v in fields.items():
            self.assertEqual(getattr(legoset, k), v)
        self.assertEqual(legoset.minifigures, None)

    def test_legoset_price_per_element_correct(self):
        """Test price per element property returns a correct value."""
        theme = Theme.objects.create(name='Classic')
        age_category = AgeCategory.objects.create(name='18+')
        fields = {
            'title': 'test title',
            'product_id': '10283',
            'theme': theme,
            'price': Decimal('333.33'),
            'available': True,
            'age': age_category,
            'elements': 2,
            'link': 'https://www.lego.com/pl-pl/product/nasa-space-shuttle-discovery-10283',
        }
        legoset = LegoSet.objects.create(**fields)

        self.assertEqual(legoset.price_per_element, Decimal('166.66'))