from django.urls import path

from orders.views import OrderCreateView, UserOrderListAPIView, OrderListAPIViewForAdmin, OrderDetailViewedAPIView, \
    OrderDetailAcceptedAPIView, ProductSoldApiView, OrderDeleteApiView

urlpatterns = [
    path('list', UserOrderListAPIView.as_view(), name='orders-list'),
    path('create', OrderCreateView.as_view(), name='orders-create'),
    path('list/for-admin', OrderListAPIViewForAdmin.as_view(), name='orders-list-for-admin'),
    path('<int:pk>/view', OrderDetailViewedAPIView.as_view()),
    path('<int:pk>/accepted', OrderDetailAcceptedAPIView.as_view()),
    path('<int:pk>/sold', ProductSoldApiView.as_view()),
    path('<int:pk>/delete', OrderDeleteApiView.as_view()),
]
