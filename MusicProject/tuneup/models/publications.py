
from django.conf import settings
from django.db import models


class MusicHit(models.Model):
    """ User audio story to be shared with others """
    
    title = models.CharField(max_length=50) 
    autor = models.ForeignKey("BaseUser", related_name="hit_stories")
    audio = models.FieldFile(upload_to=settings.AUDIO_FILES_FOLDER)
    cover = models.FileField(upload_to=settings.AUDIO_COVERS_FOLDER) 
    publish_date = models.DateTimeField(null=True)