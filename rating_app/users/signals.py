from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from rate.models import House


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def create_or_update_house(sender, instance, created, **kwargs):
    if created:
        House.objects.create(user=instance, name=instance.username)
    instance.house.save()





