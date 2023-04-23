import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates the super user if it doesn't exist."

    def handle(self, *args, **options):
        su_username = os.environ.get("SUPERUSER_USERNAME", None)
        su_password = os.environ.get("SUPERUSER_PASSWORD", None)

        if su_username is None or su_password is None:
            self.stdout.write(
                self.style.WARNING(
                    "SUPERUSER_USERNAME and SUPERUSER_PASSWORD environmental variables have not been set. "
                    "Aborting the superuser creation process."
                )
            )
            return

        if User.objects.filter(username=su_username).exists():
            self.stdout.write(self.style.WARNING(f"A superuser with '{su_username}' username already exists."))
            return

        User.objects.create_superuser(username=su_username, password=su_password)
        self.stdout.write(self.style.SUCCESS(f"A superuser with '{su_username}' has been created."))
