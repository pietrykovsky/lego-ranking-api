from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.functions import Round
from django.db.models import ExpressionWrapper, F, DecimalField

from django_celery_beat.models import CrontabSchedule, IntervalSchedule, PeriodicTask

from legoscraper.models import LegoSet, Theme, AgeCategory

class LegoAdminSite(admin.AdminSite):
    """Custom admin panel display."""
    site_header = 'Lego Ranking Admin Panel'
    site_title = 'Lego Ranking Administation'
    index_title = site_title

class LegoSetAdmin(admin.ModelAdmin):
    """Custom lego set display in admin panel."""
    empty_value_display = 'None'
    readonly_fields = ('updated', 'price_per_element', 'available')
    list_display = ('title', 'theme', 'price', 'elements', 'price_per_element', 'available', 'updated')
    list_filter = ('theme__name', 'age__name', 'available')
    search_field = ('title', 'theme__name')

    @admin.display(ordering='price_per_element', empty_value='???')
    def price_per_element(self, obj):
        return obj.price_per_element

    def get_queryset(self, request):
        """Return the lego set queryset ordered by price per element ratio ascending."""
        queryset = LegoSet.objects.annotate(price_per_element=ExpressionWrapper(Round(F('price')/F('elements'), 2), output_field=DecimalField())).order_by('price_per_element')

        return queryset

lego_admin = LegoAdminSite(name = 'lego-admin')

lego_admin.register(LegoSet, LegoSetAdmin)
lego_admin.register(Theme)
lego_admin.register(AgeCategory)
lego_admin.register(PeriodicTask)
lego_admin.register(CrontabSchedule)
lego_admin.register(IntervalSchedule)
lego_admin.register(User)