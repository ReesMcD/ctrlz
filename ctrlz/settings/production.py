import os
from .base import *
import environ
import dj_database_url


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
env.read_env()

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
DATABASES['default'] = dj_database_url.config()

try:
    from .local import *
except ImportError:
    pass
