"""
Settings for local development environment
"""

from .base import *

DEBUG = True

SECRET_KEY = get_env_variable('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'crm_easy_db',
        'USER': 'jp',
        'PASSWORD': DB_PASS,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS += ['debug_toolbar',]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
