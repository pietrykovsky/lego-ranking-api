from rest_framework import routers

from .views import LegoSetViewSet

router = routers.DefaultRouter()
router.register('legosets', LegoSetViewSet)
urlpatterns = router.urls