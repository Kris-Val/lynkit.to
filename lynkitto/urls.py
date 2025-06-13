from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from rest_framework.routers import DefaultRouter
from django.urls import path, re_path

from profiles.views import LinkViewSet, ProfileViewSet
from users.views import home, logout_view

from .views import homepage

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

sitemaps = {}

router = DefaultRouter()
router.register(r"profile", ProfileViewSet, basename="profile")
router.register(r"links", LinkViewSet, basename="link")
# router.register(r"users", User, basename="user")

api_v1_patterns = [
    path("", include(router.urls)),
]

urlpatterns = [
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('accounts/', include('allauth.socialaccount.urls')),
    path("_allauth/", include("allauth.headless.urls")),
    path("api/v1/", include((api_v1_patterns, "api"), namespace="v1")),
    path("api/schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
    path("docs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("users", include("users.urls")),
    re_path(r'^(?:.*)/?$', homepage),  # optional: handles React/Next client-side routing
    path('', homepage)

]

if settings.DEBUG:
    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

    urlpatterns = [
                      path("404/", TemplateView.as_view(template_name="404.html")),
                      path("500/", TemplateView.as_view(template_name="500.html")),
                  ] + urlpatterns

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
