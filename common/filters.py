import django_filters

from common.models import Brand


class BrandFilter(django_filters.FilterSet):
    field_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Brand
        fields = ['name']
