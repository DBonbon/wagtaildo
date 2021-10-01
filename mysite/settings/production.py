from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '157.230.20.7']

try:
    from .local import *
except ImportError:
    pass
