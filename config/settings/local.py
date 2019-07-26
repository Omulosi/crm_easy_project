"""
Settings for local development environment
"""

from .base import *

DEBUG = True

SECRET_KEY = env("SECRET_KEY", default="nfekhrf84jfjfi9rjr%$343")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


# INSTALLED_APPS += ['debug_toolbar',]

# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
