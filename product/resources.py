from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from product.models import Product


class ProductResource(resources.ModelResource):
    id = Field(attribute="id", column_name="ID", readonly=True)
    name = Field(attribute="name", column_name="Nomi")

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
        ]
