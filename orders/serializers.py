from rest_framework import serializers

from cart.serializers import CartCreateSerializer, CartSerializerForOrder
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
    cart = CartSerializerForOrder(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'user', 'name', 'phone', 'region', 'city', 'village', 'address', 'job_address', 'addition', 'promo_kod',
            'pyment', 'date', 'cart')
