from rest_framework import serializers

from cart.models import Cart
from product.models import Product
from product.serializers import ProductForCartSerializer, ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    product = ProductForCartSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'price', 'quantity', 'created_at', 'total_price', 'total_quantity']


class CartSerializerForOrder(serializers.ModelSerializer):
    # product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'quantity']


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product', 'quantity', 'total_price']
