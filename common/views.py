from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from paginations import CustomPageNumberPagination
from product.models import Product
from .filters import BrandFilter, CategoryFilter
from .models import Category, Brand
from common.serializers import CategorySerializer, BrandSerializer
from product.serializers import ProductSerializer


# Create your views here.


class BaseCategoryView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None).order_by('id')
    serializer_class = CategorySerializer


class CategoryProductView(APIView, CustomPageNumberPagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['price', 'rating', 'updated_year']
    search_fields = ['name']
    filterset_class = CategoryFilter
    serializer_class = ProductSerializer

    @swagger_auto_schema(method='get')
    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
            products = Product.objects.filter(category=category)
            if category.parent is None:
                child_categories = category.child_category.all()
                products = Product.objects.filter(category__in=child_categories)

            order_by = request.GET.get('ordering')

            if order_by == 'price':
                products = products.order_by('price')
            elif order_by == '-price':
                products = products.order_by('-price')
            elif order_by == 'rating':
                products = products.order_by('-average_rating')
            elif order_by == 'updated_year':
                products = products.order_by('-updated_year')

            filter_set = CategoryFilter(request.GET, queryset=products)

            page = self.paginate_queryset(filter_set.qs)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.serializer_class(filter_set.qs, many=True)
            return Response(serializer.data)
            # ----
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)


class BrandProductView(APIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['price', 'rating', 'updated_year']
    search_fields = ['name']
    filterset_class = BrandFilter

    @swagger_auto_schema(method='get')
    def get(self, request, slug):
        try:
            brand = Brand.objects.get(slug=slug)
            products = Product.objects.filter(brand=brand)

            order_by = request.GET.get('ordering')
            search = request.GET.get('search')

            if search:
                products = products.filter(name__icontains=search)
            if order_by == '-price':
                products = products.order_by('-price')
            elif order_by == 'price':
                products = products.order_by('price')
            elif order_by == 'rating':
                products = products.order_by('-average_rating')
            elif order_by == 'updated_year':
                products = products.order_by('-updated_year')

            filter_set = BrandFilter(request.GET, queryset=products)
            serializer = ProductSerializer(filter_set.qs, many=True)

            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Brand not found'}, status=status.HTTP_404_NOT_FOUND)


class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
