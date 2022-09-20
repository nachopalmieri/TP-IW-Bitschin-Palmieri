
from django.db import models
from django.db.models.fields.files import FieldFile
from django.conf import settings
from tuneup.files.audio import AudioFile


class FieldAudioFile(AudioFile, FieldFile):
    pass


class AudioFileField(models.FileField):
    attr_class = FieldAudioFile 
    upload_to = settings.AUDIO_FILES_FOLDER