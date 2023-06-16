from datetime import timedelta

from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver
from users.models import User


@receiver(post_save, sender=User)
def create_user_data(sender, instance, created, **kwargs):
    pass



