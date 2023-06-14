from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from product.models import Product
from product.serializers import ProductForCartSerializer
from .models import Order
from .serializers import OrderSerializer, UserOrderSerializer


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


class UserOrderListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        order = Order.objects.get(user=user)
        if order.is_sold:
            cart = Cart.objects.filter(user=user)
            product = Product.objects.filter(cart_products__in=cart)
            serializer = ProductForCartSerializer(product, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class OrderListAPIViewForAdmin(generics.ListAPIView):
    serializer_class = UserOrderSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = Order.objects.order_by('date')
        return queryset


class OrderDetailViewedAPIView(APIView):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        order.is_viewed = True
        order.save()
        serializer = UserOrderSerializer(order)
        return Response(serializer.data)


class OrderDetailAcceptedAPIView(APIView):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        order.is_accepted = True
        order.save()
        return Response(status=status.HTTP_202_ACCEPTED)


class ProductSoldApiView(APIView):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        order.is_sold = True
        order.save()
        user = order.user
        carts = Cart.objects.filter(user=user)
        for cart in carts:
            quantity = cart.quantity
            product = cart.product
            product.count -= quantity
            product.save()
        carts.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class OrderDeleteApiView(APIView):
    def delete(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
