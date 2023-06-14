from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Category(models.Model):
    title = models.CharField(_("Name"), max_length=255)
    slug = models.CharField(max_length=255, blank=True, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="child_category")

    def __str__(self):
        return str(self.title)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.title.upper():
            self.slug = slugify(self.title.lower())
        return super().save(force_insert, force_update, using, update_fields)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True, unique=True)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.name.upper():
            self.slug = slugify(self.name.lower())
        return super().save(force_insert, force_update, using, update_fields)
