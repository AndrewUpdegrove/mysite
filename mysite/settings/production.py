from .base import *
import os

DEBUG = False

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
