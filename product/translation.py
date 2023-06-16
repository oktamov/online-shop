from modeltranslation.translator import translator, TranslationOptions

from product.models import Product, SpecificationName, SpecificationAttribute


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class SpecificationNameTranslationOptions(TranslationOptions):
    fields = ('name',)


class SpecificationValueTranslationOptions(TranslationOptions):
    fields = ('value',)


translator.register(Product, ProductTranslationOptions)
translator.register(SpecificationName, SpecificationNameTranslationOptions)
translator.register(SpecificationAttribute, SpecificationValueTranslationOptions)
