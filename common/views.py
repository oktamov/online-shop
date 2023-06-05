from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from .filters import BrandFilter
from .models import Category, Brand
from common.serializers import CategorySerializer, BrandSerializer, ChildCategory
from product.serializers import ProductSerializer


# Create your views here.


class BaseCategoryView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None).order_by('id')
    serializer_class = CategorySerializer


class CategoryProductView(APIView):
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ("title", "slug", "category__title", "brand__title")

    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
            products = Product.objects.filter(category=category)
            if category.parent is None:
                child_categories = category.child_category.all()
                products = Product.objects.filter(category__in=child_categories)

            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)


class BrandProductView(APIView):
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['brand__product_price']  # Specify the fields you want to allow ordering on
    search_fields = ['name']  # Specify the fields you want to allow searching on

    def get(self, request, slug):
        try:
            brand = Brand.objects.get(slug=slug)
            products = Product.objects.filter(brand=brand)
            filter_set = BrandFilter(request.GET, queryset=products)
            serializer = BrandSerializer(filter_set.qs, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Brand not found'}, status=status.HTTP_404_NOT_FOUND)


class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
