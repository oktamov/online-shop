from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from product_smartphone_gadjet.models import Category, Brand, Smartphone
from common.serializers import CategorySerializer, BrandSerializer, ChildCategory
from product_smartphone_gadjet.serializers import SmartphoneSerializer


# Create your views here.


class BaseCategoryView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None).order_by('id')
    serializer_class = CategorySerializer


class CategoryProductView(APIView):
    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
            products = Smartphone.objects.filter(category=category)
            serializer = SmartphoneSerializer(products, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)


class BrandProductView(APIView):
    def get(self, request, slug):
        try:
            brand = Brand.objects.get(slug=slug)
            products = Smartphone.objects.filter(brand=brand)
            serializer = SmartphoneSerializer(products, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Brand not found'}, status=status.HTTP_404_NOT_FOUND)


class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
