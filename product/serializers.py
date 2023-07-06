from rest_framework import serializers

from product.models import Product, Rating, ProductImages


class RatingForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "product", "comment", "ratings", "average_rating")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ("image",)


class ProductSerializer(serializers.ModelSerializer):
    product_image = ImageSerializer(many=True, read_only=True)
    liked = serializers.SerializerMethodField()

    def get_liked(self, obj):
        user = self.context['request'].user
        return obj.liked.filter(id=user.id).exists()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'category', 'brand', 'sales_price', 'liked', 'num_likes', 'average_rating', 'product_image']


class ProductForLikedSerializer(serializers.ModelSerializer):
    product_image = ImageSerializer(many=True, read_only=True)
    liked = serializers.SerializerMethodField()

    def get_liked(self, obj):
        user = self.context['request'].user
        return obj.liked.filter(id=user.id).exists()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'category', 'brand', 'sales_price', 'liked', 'product_image']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "product", "comment", 'ratings']


class ProductForCartSerializer(serializers.ModelSerializer):
    product_image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'sales_price', 'product_image']


class ImportFileSerializer(serializers.Serializer):
    file = serializers.FileField()