from django.contrib import admin

from product.models import Product, Rating, SpecificationAttribute, Specification, ProductImages

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Rating)
admin.site.register(Specification)
admin.site.register(SpecificationAttribute)
