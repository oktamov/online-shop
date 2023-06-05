from django.urls import path, include
from .views import ProductListView, ProductDetailView, RatingView, ProductLikedView, ProductLikedList

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('<slug:slug>/like', ProductLikedView.as_view(), name='product-like-unlike'),
    path('liked/list', ProductLikedList.as_view(), name='product-liked-list'),
    path('reviews/create', RatingView.as_view(), name='product-reviews'),
]
