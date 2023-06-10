from django.urls import path

from orders.views import OrderView, OrderCreateView, UserOrderListAPIView

urlpatterns = [
    path('list', UserOrderListAPIView.as_view()),
    path('create', OrderCreateView.as_view()),
]
