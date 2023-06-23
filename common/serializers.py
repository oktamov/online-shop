from rest_framework import serializers

from .models import Category, Brand


class ChildCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    child_category = ChildCategory(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'child_category']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'image']
