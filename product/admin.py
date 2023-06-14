from django.contrib import admin

from product.models import Product, Rating, SpecificationAttribute, ProductImages, SpecificationName

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Rating)
admin.site.register(SpecificationName)
admin.site.register(SpecificationAttribute)
