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


class UserOrderListAPIView(generics.ListAPIView):
    serializer_class = UserOrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


# class OrderCreateView(APIView):
#     def post(self, request, serializer):
#         serializer = UserOrderSerializer(data=self.request.data)
#         if serializer.is_valid():
#             order = serializer.save()
#             return Response("Order created successfully.", status=201)
#         return Response(serializer.errors, status=400)
