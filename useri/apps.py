from django.apps import AppConfig


class UseriAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'useri'

    def ready(self):
        import useri.signals
