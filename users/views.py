from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    """Render the home page."""
    return render(request, "home.html")


def logout_view(request):
    """Handle user logout."""
    logout(request)
    return redirect("/")  # Redirect to home page after logout
