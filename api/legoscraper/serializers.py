from rest_framework import serializers

from .models import LegoSet, AgeCategory, Theme

class ThemeSerializer(serializers.ModelSerializer):
    """Serializer for theme category."""

    class Meta:
        model = Theme
        fields = ['id', 'name']
        read_only_fields = fields

class AgeCategorySerializer(serializers.ModelSerializer):
    """Serializer for age category."""

    class Meta:
        model = AgeCategory
        fields = ['id', 'name']
        read_only_fields = fields

class LegoSetSerializer(serializers.ModelSerializer):
    """Serializer for lego set."""
    theme = ThemeSerializer
    age = AgeCategorySerializer

    class Meta:
        model = LegoSet
        fields = ['id', 'title', 'product_id', 'price', 'elements', 'theme', 'age', 'available', 'minifigures', 'link']
        read_only_fields = fields