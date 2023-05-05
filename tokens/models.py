from django.contrib.auth.models import User
from django.db import models


class TokenProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s token profile"
