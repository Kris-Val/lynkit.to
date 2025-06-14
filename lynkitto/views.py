from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


def homepage(request):
    """
    A simple view that returns a welcome message.
    """
    return render(request, "next/index.html")
