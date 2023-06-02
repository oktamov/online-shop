from rest_framework import serializers

from product_smartphone_gadjet.models import Smartphone


class SmartphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartphone
        fields = ('id', 'title', 'slug', 'description', 'brand', 'category', 'storage')
