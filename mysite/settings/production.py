from .base import *

DEBUG = True # int(os.environ.get("DEBUG", default=1))
SECRET_KEY = 'django-insecure-wt2^elcpvn+a-aa7exnt92ak#l%yozhx+!el^^g1o&z246vyyb' # os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ['*'] # os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# try:
#     from .local import *
# except ImportError:
#     pass
