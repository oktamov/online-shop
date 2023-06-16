from django.db import models

from users.models import User

PAYMENT_METHODS = [
    ('Naqd pul', 'Naqd'),
    ('Karta', 'Karta'),

]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    region = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    village = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    job_address = models.CharField(max_length=50, null=True, blank=True)
    addition = models.CharField(max_length=255, null=True, blank=True)
    promo_kod = models.CharField(max_length=10, null=True, blank=True)
    pyment = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    date = models.DateTimeField(auto_now_add=True)
    is_viewed = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)

# /orders/<id>/
# {
#     "is_sold": False,
# }
