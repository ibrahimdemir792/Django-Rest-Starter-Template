"""
Settings package initialization.

Imports from the appropriate settings module based on DJANGO_SETTINGS_MODULE.
When DJANGO_SETTINGS_MODULE is set to "api.settings" (the default in manage.py),
this file auto-selects development settings. For production, set
DJANGO_SETTINGS_MODULE=api.settings.production in your environment.
"""

import os

env = os.environ.get("DJANGO_SETTINGS_MODULE", "api.settings")

if env == "api.settings":
    from api.settings.development import *  # noqa: F401, F403
