import random
import string

from django.contrib.auth.models import User
from django.db import models

STREAM_KEY_LENGTH = 32


def generate_stream_key():
    letters_and_digits = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters_and_digits) for _ in range(STREAM_KEY_LENGTH))


class StreamProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stream_key = models.CharField(max_length=32, default=generate_stream_key)
    url = models.CharField(max_length=256, blank=True, null=True)
    title = models.CharField(max_length=128, default="Just another stream")
    description = models.TextField(max_length=512, default="", blank=True)
    is_streaming = models.BooleanField(default=False)
    viewers = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s stream profile"
