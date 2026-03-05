import django_filters
from .models import Property


class PropertyFilter(django_filters.FilterSet):

    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Property
        fields = ["region", "city", "rooms", "property_type"]