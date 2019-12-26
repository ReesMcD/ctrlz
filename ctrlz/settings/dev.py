from .base import *
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.environ['DEBUG']
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
