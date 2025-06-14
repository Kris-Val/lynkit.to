from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django_nextjs.render import render_nextjs_page


async def index(request):
    """Render the home page."""
    return await render_nextjs_page(request)
