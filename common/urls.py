from django.urls import path

from common.views import BaseCategoryView, BrandView, CategoryProductView, BrandProductView

urlpatterns = [
    path('category', BaseCategoryView.as_view(), name='category-list'),
    path('category/<slug:slug>', CategoryProductView.as_view(), name='category-detail'),
    path('brand/<slug:slug>', BrandProductView.as_view(), name='brand-detail'),
    path('brand', BrandView.as_view(), name='brand-list'),
]
