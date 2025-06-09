import environ

# Build paths inside the project like this: root("path/to/file")
root = environ.Path(__file__) - 2

# Set casting types and default values.
env = environ.Env(
    DEBUG=(bool, False),
    ENABLE_DEBUG_TOOLBAR=(bool, False),
    ADD_FULL_SUBNET_TO_INTERNAL_IPS=(bool, False),
)

env.read_env(root(".env"))

# PROJECT
# ----------------------------------------------------------------------

DOMAIN = env("DOMAIN")

INTERNAL_IPS = ["127.0.0.1", "::1"]

DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="noreply@" + DOMAIN)

CLIENT_EMAIL = env("CLIENT_EMAIL", default=DEFAULT_FROM_EMAIL)

SERVER_EMAIL = env("SERVER_EMAIL", default="django@fluxility.com")

EMAIL_CONFIG = env.email_url()

vars().update(EMAIL_CONFIG)

# GENERAL
# ----------------------------------------------------------------------

DEBUG = env("DEBUG")

NODE_ENV = env("NODE_ENV", default="production")

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

SITE_ID = env.int("SITE_ID", default=1)

X_FRAME_OPTIONS = "DENY"

FILE_UPLOAD_PERMISSIONS = 0o644

# I18N & L10N
# ----------------------------------------------------------------------

LANGUAGE_CODE = "en-us"  # or 'nl' for Dutch, etc.

LANGUAGES = [
    ("en", "English"),
    ("nl", "Dutch"),
    ("fr", "French"),
]
TIME_ZONE = "Europe/Amsterdam"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [root("locale/")]

# AUTHENTICATION
# ----------------------------------------------------------------------

LOGIN_REDIRECT_URL = "/"

# DATABASES & CACHES
# ----------------------------------------------------------------------

DATABASES = {"default": env.db()}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

CACHES = {"default": env.cache()}

# URLS
# ----------------------------------------------------------------------

ROOT_URLCONF = "lynkitto.urls"

WSGI_APPLICATION = "lynkitto.wsgi.application"

# APPS
# ----------------------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.redirects",
    "rest_framework",
    "lynkitto",
    "sekizai",
    "adminsortable2",
    "easy_thumbnails",
    "django_recaptcha",
    "dbsettings",
    "contrib.admin_site_checks",
    "profiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.headless",
    "corsheaders",
]

# MIDDLEWARE
# ----------------------------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# STATIC
# ----------------------------------------------------------------------

STATIC_ROOT = env("STATIC_ROOT", default=root(".static"))

STATIC_URL = "/static/"

STATICFILES_DIRS = [root("lynkitto/static", required=True)]

# MEDIA
# ----------------------------------------------------------------------

MEDIA_URL = "/media/"

MEDIA_ROOT = env("MEDIA_ROOT", default=root(".media"))

# DATA
# ----------------------------------------------------------------------

DATA_ROOT = env("DATA_ROOT", default=root(".data"))

data_dir = root.path(DATA_ROOT)

# RATE LIMITING
# ----------------------------------------------------------------------

# REST_FRAMEWORK = {
#     "DEFAULT_THROTTLE_CLASSES": [
#         "centraal_register_techniek.throttling.AnonBurstRateThrottle",
#         "centraal_register_techniek.throttling.AnonSustainedRateThrottle",
#         "centraal_register_techniek.throttling.UserBurstRateThrottle",
#         "centraal_register_techniek.throttling.UserSustainedRateThrottle",
#     ],
#     "DEFAULT_THROTTLE_RATES": {
#         "anon_burst": "100/minute",
#         "anon_sustained": "1000/hour",
#         "user_burst": "200/minute",
#         "user_sustained": "2000/hour",
#     },
# }
REST = _FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
}

# CORS
# ----------------------------------------------------------------------
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_HTTPONLY = False
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://127.0.0.1:3000",
    "http://0.0.0.0",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://127.0.0.1:3000",
    "https://127.0.0.1:3000",
    "http://0.0.0.0",
]
CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True

# AllAuth
# ----------------------------------------------------------------------
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_METHODS = {"email"}
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
# ACCOUNT_LOGIN_BY_CODE_ENABLED = True
# ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
# ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
EMAIL_HOST = "mail"
EMAIL_PORT = 1025
HEADLESS_ONLY = True
# HEADLESS_FRONTEND_URLS = {
#     "account_confirm_email": "/account/verify-email/{key}",
#     "account_reset_password": "/account/password/reset",
#     "account_reset_password_from_key": "/account/password/reset/key/{key}",
#     "account_signup": "/account/signup",
#     "socialaccount_login_error": "/account/provider/callback",
# }


# TEMPLATES
# ----------------------------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [root("lynkitto/static/", required=True)],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
            ]
        },
    }
]

# PASSWORDS
# ----------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# SENTRY
# ----------------------------------------------------------------------

if not DEBUG:
    SENTRY_DSN = env("SENTRY_DSN")

    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[DjangoIntegration()])

# TESTING
# ----------------------------------------------------------------------

# Allow connections from any device on the network. Used for testing
# on mobile devices.
if DEBUG and env.get_value("ADD_FULL_SUBNET_TO_INTERNAL_IPS", False):
    import socket

    my_ip_address = socket.gethostbyname(socket.gethostname())
    my_ip_subnet = my_ip_address.rsplit(".", 1)[0]

    INTERNAL_IPS = ["127.0.0.1", "::1"]
    ALLOWED_HOSTS = ["*"]

    for i in range(0, 256):
        INTERNAL_IPS.append(f"{my_ip_subnet}.{i}")

# DEBUG TOOLBAR
# ----------------------------------------------------------------------

if DEBUG and env.get_value("ENABLE_DEBUG_TOOLBAR", False):
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

# NAOMI
# ----------------------------------------------------------------------

if DEBUG:
    try:
        from naomi.mail.backends import naomi  # noqa: F401
    except ImportError:
        pass
    else:
        INSTALLED_APPS += ("naomi",)

        EMAIL_BACKEND = "naomi.mail.backends.naomi.NaomiBackend"
        EMAIL_FILE_PATH = root(".naomi/")

SILENCED_SYSTEM_CHECKS = ["django_recaptcha.recaptcha_test_key_error"]
