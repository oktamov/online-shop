from django.db import models

from orders.models import Order
from product.models import Product
from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_products')
    price = models.FloatField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        cart_items = Cart.objects.filter(user=self.user)
        total = sum(item.price for item in cart_items)
        return total

    @property
    def total_quantity(self):
        cart_items = Cart.objects.filter(user=self.user)
        total = sum(item.quantity for item in cart_items)
        return total

    def save(self, *args, **kwargs):
        self.price = self.quantity * self.product.price
        super().save(*args, **kwargs)
