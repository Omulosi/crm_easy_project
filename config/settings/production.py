from .base import *
from .base import env

DEBUG = False

DATABASES['default'] = env.db('DATABASE_URL')
DATABASES['default']['ATOMIC_REQUESTS'] = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = env('SECRET_KEY')

django_heroku.settings(locals())
