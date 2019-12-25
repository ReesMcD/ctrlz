import os
from .base import *

DEBUG = False

try:
    from .local import *

    env = os.environ.copy()
    SECRET_KEY = env['SECRET_KEY']

    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

    COMPRESS_OFFLINE = True
    COMPRESS_CSS_FILTERS = [
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.CSSMinFilter',
    ]
    COMPRESS_CSS_HASHING_METHOD = 'content'

except ImportError:
    pass
