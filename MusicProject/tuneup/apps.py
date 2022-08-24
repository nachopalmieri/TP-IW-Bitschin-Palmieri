from django.apps import AppConfig
from . import settings

class TuneupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tuneup'
