from django.urls import path

from product_smartphone_gadjet.views import PhoneListView

urlpatterns = [
    path('phone', PhoneListView.as_view(), name='phone-list')
]
