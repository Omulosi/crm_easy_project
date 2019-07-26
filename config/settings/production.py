from .base import *
from .base import DATABASES

import dj_database_url

DEBUG = False

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['*']
