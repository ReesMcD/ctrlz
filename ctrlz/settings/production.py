import os
from .base import *
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.environ['DEBUG']
SECRET_KEY = os.environ['SECRET_KEY']
DATABASES['default'] = dj_database_url.config()

try:
    from .local import *
except ImportError:
    pass
