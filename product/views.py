from datetime import datetime
from io import BytesIO

import pandas as pd
from django.http import FileResponse
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from paginations import CustomPageNumberPagination
from .filters import ProductFilter
from .serializers import ProductSerializer, RatingSerializer, ImportFileSerializer
from .models import Product, Rating, SpecificationAttribute


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = ProductFilter
    ordering_fields = ("price", 'average_rating', 'updated_year', 'discount')
    search_fields = ("name", "slug", "category__title", "brand__name")
    pagination_class = CustomPageNumberPagination


class ProductDetailView(APIView):
    def get(self, request, slug):
        attributes_list = []
        try:
            product = Product.objects.get(slug=slug)
            specification_attributes = SpecificationAttribute.objects.filter(
                product=product)
            attribute_dict = {attr.name.name: attr.value for attr in specification_attributes}

            ratings = product.rating.all()
            images = product.product_image.values_list('image', flat=True)
            attributes_list.append(attribute_dict)
            ratings_list = []
            for rating in ratings:
                rating_dict = {
                    'comment': rating.comment,
                    'rating': rating.ratings,
                    'average_rating': rating.average_rating
                }
                ratings_list.append(rating_dict)

            product_data = {
                'name': product.name,
                'slug': product.slug,
                'category': product.category.title,
                'brand': product.brand.name,
                'description': product.description,
                'count': product.count,
                'price': product.price,
                'discount': product.discount,
                'views': product.views,
                'likes_num': product.num_likes,
                'updated_year': product.updated_year,
                'images': images,
                'attributes': attributes_list,
                'ratings': ratings_list,
            }
            product.views += 1
            product.save()

            return Response(product_data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)


class RatingView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ProductLikedView(APIView):
    def post(self, request, slug):
        try:
            product = Product.objects.get(slug=slug)
            user = request.user
            if not user.is_authenticated:
                return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

            if user in product.liked.all():
                product.liked.remove(user)
                liked = False
            else:
                product.liked.add(user)
                liked = True

            product.save()

            return Response({'liked': liked}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)


class ProductLikedList(APIView):
    def get(self, request):
        liked_product = Product.objects.filter(liked__phone_number=request.user.phone_number)
        serializer = ProductSerializer(liked_product, many=True, context={'request': request})
        return Response(serializer.data)


class ProductExportView(APIView):
    def get(self, request):
        columns = {
            "id": "ID",
            "name": "Nomi"
        }
        df = pd.DataFrame(
            list(
                Product.objects.values(
                    "id", "name"
                )
            ),
            columns=list(columns.keys())
        )
        df.rename(columns=columns, inplace=True)

        file_like_object = BytesIO()
        df.to_excel(file_like_object, index=False)
        file_like_object.seek(0)  # move to the beginning of file
        response = FileResponse(file_like_object)
        filename = f"Courses_{datetime.now().strftime('%Y%m%d_%H%M')}"
        response['Content-Disposition'] = f'attachment; filename="{filename}.xlsx"'

        return response


class ProductImportView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(request_body=ImportFileSerializer)
    def post(self, request):
        serializer = ImportFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = request.FILES.get("file")
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            Product.objects.update_or_create(id=row["ID"], defaults={
                "name": row["Nomi"]
            })
        return Response("Course import started.")
