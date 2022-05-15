from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from first_app.models import Profile


@receiver(post_save, sender=User)
def created_profile(sender, instance, created, *args, **kwargs):
    if not created:
        return

    profile = Profile(user=instance)
    profile.save()