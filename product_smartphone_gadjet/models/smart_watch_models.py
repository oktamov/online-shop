from django.db import models
from django.utils.text import slugify

from common.models import Brand, Category


# Create your models here.


class SmartWatch(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="smart_watch_brand")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="smart_watch_category")

    def __str__(self):
        return str(self.title)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.title.upper():
            self.slug = slugify(self.title.lower())
        return super().save(force_insert, force_update, using, update_fields)
