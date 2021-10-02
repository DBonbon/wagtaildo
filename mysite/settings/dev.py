from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wt2^elcpvn+a-aa7exnt92ak#l%yozhx+!el^^g1o&z246vyyb'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] # ['localhost', '157.230.20.7']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")

try:
    from .local import *
except ImportError:
    pass
