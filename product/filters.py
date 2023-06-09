from django_filters import rest_framework as filters

from product.models import Product


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    brand = filters.CharFilter(field_name='brand__name', lookup_expr='icontains')
    spefication_name = filters.CharFilter(field_name='specification_attributes__name__name', lookup_expr='icontains')
    spefication_attribute = filters.CharFilter(field_name='specification_attributes__value', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'brand']
