from rest_framework import generics, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from product.models import Product
from product.serializers import ProductForCartSerializer
from .models import Order
from .serializers import UserOrderSerializer


class UserOrderListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        order = Order.objects.filter(user=user, is_sold=True)
        if order:
            cart = Cart.objects.filter(user=user, order__in=order)
            product = Product.objects.filter(cart_products__in=cart)
            serializer = ProductForCartSerializer(product, many=True)
            return Response(serializer.data)
        return Response({'status': "sizda sotib olingan mahsulotlar yoq"})


class OrderCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = UserOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get("name")
        phone = serializer.validated_data.get("phone")
        region = serializer.validated_data.get("region")
        city = serializer.validated_data.get("city")
        village = serializer.validated_data.get("village")
        address = serializer.validated_data.get("address")
        job_address = serializer.validated_data.get("job_address")
        addition = serializer.validated_data.get("addition")
        promo_kod = serializer.validated_data.get("promo_kod")
        pyment = serializer.validated_data.get("pyment")
        carts = Cart.objects.filter(user=request.user, order=None)
        if not carts:
            return Response({'status': "avval mahsulotni savatchaga qoshing"})

        order = Order.objects.create(user=request.user, name=name, phone=phone, region=region, city=city,
                                     village=village, address=address, job_address=job_address, addition=addition,
                                     promo_kod=promo_kod, pyment=pyment)
        for cart in carts:
            cart.order = order
            cart.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
