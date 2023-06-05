from rest_framework import serializers

from product.models import Product, Rating, ProductImages


class RatingForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "product", "comment", "average_rating")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ("image",)


class ProductSerializer(serializers.ModelSerializer):
    rating = RatingForProductSerializer(many=True, read_only=True)
    product_image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'category', 'brand','price', 'rating', 'product_image']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "product", "comment", 'ratings']
