from rest_framework import serializers

from cart.models import Cart
from cart.serializers import CartCreateSerializer, CartSerializer
from product.serializers import ProductSerializer
from users.serializers import UserSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    orders_cart = CartCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'orders_cart', 'user', 'name']


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'name']


class UserOrderSerializer(serializers.ModelSerializer):
    cart_products = CartSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'user', 'name', 'phone', 'region', 'city', 'village', 'address', 'job_address', 'addition', 'promo_kod',
            'pyment', 'date', 'cart_products')
