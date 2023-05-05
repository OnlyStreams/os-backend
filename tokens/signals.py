from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from tokens.models import TokenProfile

REG = "tokens/signals.py registered"


@receiver(post_save, sender=User)
def user_create(sender, instance, created, raw, using, **kwargs):
    if created:
        TokenProfile.objects.create(user=instance)
