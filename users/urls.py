# urls.py
from django.urls import path

from .views import auth_status

urlpatterns = [
    path("auth/status", auth_status, name="auth_status"),
]
