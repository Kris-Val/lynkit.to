from django.apps import AppConfig
from django.core.checks import register


class AdminSiteConfig(AppConfig):
    name = "contrib.admin_site_checks"

    def ready(self):
        from .checks import check_admin_site_models

        register(check_admin_site_models)
