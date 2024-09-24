from django.apps import AppConfig


class UserbioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userbio'


class YourAppConfig(AppConfig):
    name = 'your_app_name'

    def ready(self):
        import your_app_name.signals