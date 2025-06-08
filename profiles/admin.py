from django.contrib import admin

from .models import Link, Profile

admin.site.register([Profile, Link])
