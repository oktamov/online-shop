from rest_framework import generics

from product_smartphone_gadjet.models import Smartphone
from product_smartphone_gadjet.serializers import SmartphoneSerializer


class PhoneListView(generics.ListAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
