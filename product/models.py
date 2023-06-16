from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from common.models import Category, Brand
from users.models import User


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    slug = models.CharField(max_length=255, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_product")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand_product")
    description = models.TextField(_("Description"), blank=True)
    count = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    sales_price = models.FloatField(default=0, blank=True)
    discount = models.IntegerField(default=0, blank=True, null=True)
    views = models.IntegerField(default=0)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    updated_year = models.DateTimeField(auto_now=True)
    average_rating = models.FloatField(default=0)

    def __str__(self):
        return self.name

    @property
    def num_likes(self):
        return self.liked.all().count()

    def update_average_rating(self):
        ratings_sum = self.rating.aggregate(total=models.Sum('ratings'))['total']
        ratings_count = self.rating.count()

        if ratings_sum is None or ratings_count == 0:
            self.average_rating = 0
        else:
            self.average_rating = ratings_sum / ratings_count

        self.save()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.name.upper():
            self.slug = slugify(self.name.lower())
        if self.discount > 0:
            self.sales_price = self.price - self.price * (self.discount / 100)
        if self.discount == 0:
            self.sales_price = self.price
        return super().save(force_insert, force_update, using, update_fields)


class SpecificationName(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name


class SpecificationAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specification_attributes')
    name = models.ForeignKey(SpecificationName, on_delete=models.CASCADE, related_name='attributes')
    value = models.CharField(_("Value"), max_length=100)

    def __str__(self):
        return f'{self.product} -> {self.name}: {self.value}'


RATING_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]


class Rating(models.Model):
    product = models.ForeignKey(Product, related_name='rating',
                                on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    ratings = models.CharField(max_length=5, choices=RATING_CHOICES, default=1)

    @property
    def average_rating(self):
        ratings_sum = self.product.rating.aggregate(total=models.Sum('ratings'))['total']
        ratings_count = self.product.rating.count()

        if ratings_sum is None or ratings_count == 0:
            return 0

        return ratings_sum / ratings_count

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.update_average_rating()


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='static/images/')
