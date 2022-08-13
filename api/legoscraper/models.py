from django.db import models

from decimal import Decimal

class LegoSet(models.Model):
    """Model for lego set objects."""

    title = models.CharField(max_length=255)
    product_id = models.CharField(max_length=50, unique=True)
    theme = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.CharField(max_length=100)
    age = models.CharField(max_length=5)
    elements = models.IntegerField()
    link = models.TextField()
    minifigures = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def price_per_element(self):
        """Return price per element ratio."""
        elements = Decimal(self.elements)
        price = Decimal(self.price)
        return Decimal(price/elements).quantize(Decimal('.01'))