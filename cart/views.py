from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.models import Product
from .serializers import CartSerializer
from .models import Cart


class CartAPIView(APIView):
    def get(self, request):
        cart_items = Cart.objects.filter(user=request.user, order=None)

        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data)


class CartCreateView(APIView):
    def post(self, request, product_pk):
        user = request.user
        product = Product.objects.get(id=product_pk)
        if product:
            if Cart.objects.filter(user=user, product=product):
                cart = Cart.objects.get(user=user, product=product)
                cart_quantity = cart.quantity
                product_count = product.count
                if cart_quantity < product_count:
                    cart.quantity += 1
                if cart_quantity == product_count:
                    return Response({"detail": "mahsulotimiz soni cheklangan"})
                cart.save()
            else:
                Cart.objects.create(user=user, product=product, quantity=1)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CartQuantityMinus(APIView):
    def put(self, request, product_pk):
        user = request.user
        product = Product.objects.get(id=product_pk)
        quantity = Cart.objects.get(user=user, product=product).quantity
        if quantity == 1:
            Cart.objects.filter(user=user, product=product).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        price = Cart.objects.get(user=user, product=product).price
        Cart.objects.update(quantity=quantity - 1, price=price - product.price)
        return Response(status=status.HTTP_200_OK)


class CartDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return None

    def get(self, request, pk):
        cart_item = self.get_object(pk)
        if cart_item is not None:
            serializer = CartSerializer(cart_item)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        cart_item = self.get_object(pk)
        if cart_item is not None:
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
