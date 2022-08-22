from django.contrib import admin

from legoscraper.models import LegoSet, Theme, AgeCategory

admin.site.register(LegoSet)
admin.site.register(Theme)
admin.site.register(AgeCategory)