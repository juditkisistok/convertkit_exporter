from django.apps import AppConfig


class SubscriberExportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscriber_export'

    def ready(self):
        import subscriber_export.signals