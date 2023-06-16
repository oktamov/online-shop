from django.db import models

from orders.models import Order
from product.models import Product
from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cart', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_products')
    price = models.FloatField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.product}"

    @property
    def total_price(self):
        cart_items = Cart.objects.filter(user=self.user, order=self.order)
        total = sum(item.price for item in cart_items)
        return total

    @property
    def total_quantity(self):
        cart_items = Cart.objects.filter(user=self.user, order=self.order)
        total = sum(item.quantity for item in cart_items)
        return total

    def save(self, *args, **kwargs):
        self.price = self.quantity * self.product.sales_price
        super().save(*args, **kwargs)
