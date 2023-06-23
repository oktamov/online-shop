from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from paginations import CustomPageNumberPagination
from product.models import Product
from .filters import BrandFilter, CategoryFilter
from .models import Category, Brand
from common.serializers import CategorySerializer, BrandSerializer
from product.serializers import ProductSerializer


class BaseCategoryView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None).order_by('id')
    serializer_class = CategorySerializer


class CategoryProductListView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['price', 'rating', 'updated_year']
    search_fields = ['name']
    filterset_class = CategoryFilter
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            products = Product.objects.filter(category=category)
            if category.parent is None:
                child_categories = category.child_category.all()
                products = Product.objects.filter(category__in=child_categories)

            order_by = self.request.GET.get('ordering')
            if order_by == 'rating':
                products = products.order_by('-average_rating')

            filter_set = CategoryFilter(self.request.GET, queryset=products)
            return filter_set.qs

        except Category.DoesNotExist:
            return Product.objects.none()


class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandProductView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['price', 'rating', 'updated_year']
    search_fields = ['name']
    filterset_class = BrandFilter
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            brand = Brand.objects.get(slug=slug)
            products = Product.objects.filter(brand=brand)

            order_by = self.request.GET.get('ordering')
            if order_by == 'rating':
                products = products.order_by('-average_rating')

            filter_set = CategoryFilter(self.request.GET, queryset=products)
            return filter_set.qs

        except Category.DoesNotExist:
            return Product.objects.none()
