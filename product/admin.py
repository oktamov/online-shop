from django.contrib import admin

from product.models import Product, Rating, SpecificationAttribute, ProductImages

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Rating)
admin.site.register(SpecificationAttribute)
