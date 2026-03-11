"""
Development-specific settings.

Used for local development with Docker or virtualenv.
"""

from api.settings.base import *  # noqa: F401, F403

DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True
