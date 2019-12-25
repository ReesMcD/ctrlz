import os
from .base import *
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env(".env.production")

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

try:
    from .local import *
except ImportError:
    pass
