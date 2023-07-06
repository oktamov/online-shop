from django.contrib import admin

from product.models import Product, Rating, SpecificationAttribute, ProductImages, SpecificationName
from import_export.admin import ImportExportModelAdmin

from product.resources import ProductResource


class BookAdmin(ImportExportModelAdmin):
    resource_classes = [ProductResource]


admin.site.register(Product, BookAdmin)

admin.site.register(ProductImages)
admin.site.register(Rating)
admin.site.register(SpecificationName)
admin.site.register(SpecificationAttribute)
