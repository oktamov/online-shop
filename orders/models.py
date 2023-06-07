from django.db import models

from product.models import Product
from users.models import User


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        order_items = self.order_item.all()
        total_price = sum(item.product.price * item.quantity for item in order_items)
        self.total_price = total_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - Customer: {self.customer.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"OrderItem {self.id} - Order: {self.order.id}, Product: {self.product.name}, Quantity: {self.quantity}"
