import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lynkitto.settings")
django_asgi_app = get_asgi_application()

from django_nextjs.asgi import NextJsMiddleware

application = NextJsMiddleware(django_asgi_app)
