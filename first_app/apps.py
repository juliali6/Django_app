from django.apps import AppConfig


class FirstAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # используется в качестве автоинкремента
    name = 'first_app'

    def ready(self):
        from . import signals