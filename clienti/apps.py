from django.apps import AppConfig


class ClientiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clienti'

    def ready(self):
        import clienti.signals
