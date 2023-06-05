from .models import Category, Brand
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin


@admin.register(Category)
class AdminCourse(TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.

admin.site.register(Brand)
