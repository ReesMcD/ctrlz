from .base import *

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
env.read_env(".env.development")

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
