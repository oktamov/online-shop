from django.urls import path

from common.views import BaseCategoryView, BrandView, CategoryProductListView, BrandProductView

urlpatterns = [
    path('category', BaseCategoryView.as_view(), name='category-list'),
    path('category/<slug:slug>/products', CategoryProductListView.as_view(), name='category-detail'),
    path('brand', BrandView.as_view(), name='brand-list'),
    path('brand/<slug:slug>/products', BrandProductView.as_view(), name='brand-detail'),

]
