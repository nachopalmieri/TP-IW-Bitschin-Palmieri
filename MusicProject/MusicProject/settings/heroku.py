
from MusicProject.settings import *
import django_heroku

# Define heroku specific settings

django_heroku.settings(locals(), logging=False)