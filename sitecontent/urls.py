from django.urls import path, re_path
from django_nextjs.views import nextjs_page

from . import views

urlpatterns = [
    path("", nextjs_page(stream=True), name="home"),
    # re_path(r"^(?:_next|__nextjs|next).*$", nextjs_page)
    #
    # re_path(r"^_next/.*", nextjs_page),  # ← needed for CSS, JS, chunks
]
