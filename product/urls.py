from django.urls import path
from .views import ProductListView, ProductDetailView, RatingView, ProductLikedView, ProductLikedList, \
    ProductExportView, \
    ProductImportView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path("export/", ProductExportView.as_view()),
    path("import/", ProductImportView.as_view()),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('reviews/create', RatingView.as_view(), name='product-reviews'),
    path('<slug:slug>/like', ProductLikedView.as_view(), name='product-like-unlike'),
    path('liked/list', ProductLikedList.as_view(), name='product-liked-list'),

]
