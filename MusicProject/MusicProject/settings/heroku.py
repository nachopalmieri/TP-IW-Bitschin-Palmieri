
from MusicProject.settings import *
import django_heroku


SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

django_heroku.settings(locals(), logging=False)