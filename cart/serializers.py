from rest_framework import serializers

from cart.models import Cart
from product.serializers import ProductSerializer
from users.serializers import UserSerializer


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'price', 'quantity', 'created_at', 'total_price', 'total_quantity']


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product', 'quantity', 'total_price']
