"""
Production settings for Railway deployment.

Requires the following environment variables:
    - SECRET_KEY
    - ALLOWED_HOSTS (comma-separated)
    - CORS_ALLOWED_ORIGINS (comma-separated)
    - PGDATABASE, PGUSER, PGPASSWORD, PGHOST, PGPORT
"""

import environ

from api.settings.base import *  # noqa: F401, F403

env = environ.Env(
    ALLOWED_HOSTS=(list, []),
    CORS_ALLOWED_ORIGINS=(list, []),
)

DEBUG = False

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

MIDDLEWARE.insert(  # noqa: F405
    MIDDLEWARE.index("django.middleware.security.SecurityMiddleware") + 1,  # noqa: F405
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS")

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
