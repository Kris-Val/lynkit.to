from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render


def homepage(request):
    """
    A simple view that returns a welcome message.
    """
    return render(request, 'next/index.html')
