from rest_framework import serializers

from cart.models import Cart
from product.serializers import ProductForCartSerializer


class CartSerializer(serializers.ModelSerializer):
    product = ProductForCartSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'price', 'quantity', 'created_at', 'total_price', 'total_quantity']


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product', 'quantity', 'total_price']
