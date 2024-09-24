from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserBio

@receiver(post_save, sender=User)
def create_user_bio(sender, instance, created, **kwargs):
    if created:
        UserBio.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_bio(sender, instance, **kwargs):
    if hasattr(instance, 'userbio'):  # Check if UserBio exists for this user
        instance.userbio.save()