from django.db import models

from decimal import Decimal

class LegoSet(models.Model):
    """Model for lego set objects."""

    title = models.CharField(max_length=255)
    product_id = models.CharField(max_length=50, unique=True)
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    available = models.BooleanField(default=False)
    age = models.ForeignKey('AgeCategory', on_delete=models.CASCADE)
    elements = models.IntegerField()
    link = models.TextField()
    minifigures = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @property
    def price_per_element(self):
        """Return price per element ratio."""
        elements = Decimal(self.elements)
        price = Decimal(self.price)
        return Decimal(price/elements).quantize(Decimal('.01'))

class Theme(models.Model):
    """Theme for filtering legosets."""
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class AgeCategory(models.Model):
    """Age category for filtering legosets."""
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name