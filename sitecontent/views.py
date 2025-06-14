from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django_nextjs.render import render_nextjs_page


async def index(request):
    """Render the home page."""
    return await render_nextjs_page(request)
