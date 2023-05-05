from django.apps import AppConfig


class TokensConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tokens"

    def ready(self):
        super().ready()

        # This import is required for receivers to be initialized.
        from . import signals

        print(signals.REG)
