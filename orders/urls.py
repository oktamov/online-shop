from django.urls import path

from orders.views import OrderCreateView, UserOrderListAPIView, OrderListAPIViewForAdmin, OrderDetailViewedAPIView, \
    OrderDetailAcceptedAPIView, ProductSoldApiView, OrderDeleteApiView

urlpatterns = [
    path('list', UserOrderListAPIView.as_view()),
    path('list/for-admin', OrderListAPIViewForAdmin.as_view()),
    path('create', OrderCreateView.as_view()),
    path('<int:pk>/view', OrderDetailViewedAPIView.as_view()),
    path('<int:pk>/accepted', OrderDetailAcceptedAPIView.as_view()),
    path('<int:pk>/sold', ProductSoldApiView.as_view()),
    path('<int:pk>/delete', OrderDeleteApiView.as_view()),
]
