from django.apps import AppConfig


class ModelBaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "contrib.model_base"
