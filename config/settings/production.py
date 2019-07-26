from .base import *
from .base import env
import dj_database_url

DEBUG = False

DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ATOMIC_REQUESTS'] = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = env('SECRET_KEY')
