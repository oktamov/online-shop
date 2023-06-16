from rest_framework import serializers

from cart.models import Cart
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

    # def create(self, validated_data):
    #     cart_products = validated_data.pop('cart', None)
    #     order = super().create(validated_data)
    #     for cart_product in cart_products:
    #         cart, _ = Cart.objects.create(user=validated_data.get('user'),
    #                                       product_id=cart_product.get('product'),
    #                                       quantity=cart_product.get('quantity')
    #                                       )
    #         cart.order = order
    #         cart.save()
