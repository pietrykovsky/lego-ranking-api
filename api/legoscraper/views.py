from drf_spectacular.utils import extend_schema_view

from rest_framework.viewsets import ReadOnlyModelViewSet

from django.shortcuts import get_object_or_404

from .serializers import LegoSetSerializer

from .models import LegoSet

@extend_schema_view()
class LegoSetViewSet(ReadOnlyModelViewSet):
    """View set for lego set api."""
    serializer_class = LegoSetSerializer
    queryset = LegoSet.objects.all()
    lookup_field = 'product_id'

    def get_queryset(self):
        queryset = sorted(self.queryset, key=lambda l: l.price_per_element)

        return queryset

    def get_object(self):
        obj = get_object_or_404(self.queryset, product_id=self.kwargs['product_id'])

        return obj