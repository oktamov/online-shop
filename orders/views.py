from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from .models import Order
from .serializers import OrderSerializer, OrderCreateSerializer, UserOrderSerializer


# Create your views here.


class OrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = UserOrderSerializer

    def get_queryset(self):
        user = self.request.user
        Cart.objects.filter(user=user).delete()
        return Order.objects.filter(user=user)


class UserOrderListAPIView(generics.ListAPIView):
    serializer_class = UserOrderSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user=user).prefetch_related('user__cart__product')
        return queryset

# class OrderCreateView(APIView):
#     def post(self, request, serializer):
#         serializer = UserOrderSerializer(data=self.request.data)
#         if serializer.is_valid():
#             order = serializer.save()
#             return Response("Order created successfully.", status=201)
#         return Response(serializer.errors, status=400)
