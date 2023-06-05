from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from paginations import CustomPageNumberPagination
from .serializers import ProductSerializer, RatingSerializer
from .models import Product, Rating


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("category__slug", "brand__slug", "specification__attributes__attribute_name",
                        "specification__attributes__attribute_value")
    ordering_fields = ("price", 'average_rating', 'updated_year')
    search_fields = ("name", "slug", "category__title", "brand__name")
    pagination_class = CustomPageNumberPagination


class ProductDetailView(APIView):
    def get(self, request, slug):
        try:
            product = Product.objects.get(slug=slug)
            specification = product.specification
            attributes = specification.attributes.all()
            ratings = product.rating.all()
            images = product.product_image.values_list('image', flat=True)
            attributes_list = []
            for attribute in attributes:
                attribute_dict = {
                    'name': attribute.attribute_name,
                    'value': attribute.attribute_value
                }
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
        liked_product = Product.objects.filter(liked__username=request.user.username)
        serializer = ProductSerializer(liked_product, many=True)
        print(liked_product)
        return Response(serializer.data)
