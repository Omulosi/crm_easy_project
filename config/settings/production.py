from .base import *
from .base import env
import dj_database_url
import os

DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ATOMIC_REQUESTS'] = True

ALLOWED_HOSTS = ['*']

