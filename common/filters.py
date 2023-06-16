from django_filters import rest_framework as filters

from product.models import Product


class BrandFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__title', lookup_expr='iexact')
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    specification_name = filters.CharFilter(field_name='specification_attributes__name__name', lookup_expr='icontains')
    specification_value = filters.CharFilter(field_name='specification_attributes__value', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price']


class CategoryFilter(filters.FilterSet):
    brand = filters.CharFilter(field_name='brand__name', lookup_expr='iexact')
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'min_price', 'max_price']
