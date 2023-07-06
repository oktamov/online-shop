from django.urls import path

from cart.views import CartAPIView, CartDetailAPIView, CartCreateView, CartQuantityMinus

urlpatterns = [
    path('', CartAPIView.as_view(), name='cart-list'),
    path('<int:product_pk>/create-plus', CartCreateView.as_view(), name='cart-create'),
    path('<int:product_pk>/quantity-minus', CartQuantityMinus.as_view(), name='cart-quantity-minus'),
    path('<int:pk>/', CartDetailAPIView.as_view(), name='cart-detail'),
]
