from modeltranslation.translator import translator, TranslationOptions

from .models import Category, Brand


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class BrandTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Category, CategoryTranslationOptions)
translator.register(Brand, BrandTranslationOptions)
