"""
Settings for local development environment
"""

from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env("SECRET_KEY", default="nfekhrf84jfjfi9rjr%$343")

# Stripe settings
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY')
SUBSCRIPTION_PRICE = 1500


ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


# INSTALLED_APPS += ['debug_toolbar',]

# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
