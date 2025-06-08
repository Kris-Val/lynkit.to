from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from rest_framework.routers import DefaultRouter

from profiles.views import LinkViewSet, ProfileViewSet

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

sitemaps = {}

router = DefaultRouter()
router.register(r"profile", ProfileViewSet, basename="profile")
router.register(r"links", LinkViewSet, basename="link")


urlpatterns = [
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api/v1/", include((router.urls, "v1"))),
    path("api/schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
    path("docs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

if settings.DEBUG:
    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

    from django.views.generic import TemplateView

    urlpatterns = [
        path("404/", TemplateView.as_view(template_name="404.html")),
        path("500/", TemplateView.as_view(template_name="500.html")),
    ] + urlpatterns

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
