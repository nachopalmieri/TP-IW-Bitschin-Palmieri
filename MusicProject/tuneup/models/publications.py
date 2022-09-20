
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db import models
from tuneup.models.fields import AudioFileField


PUB_STATE_ACTIVE = 'ACTIVE'
PUB_STATE_IN_REVIEW = 'IN_REVIEW'
PUB_STATE_DELETED = 'DELETED'

PUB_STATES = (
    (PUB_STATE_ACTIVE, _('Active')), 
    (PUB_STATE_IN_REVIEW, _('In Review')), 
    (PUB_STATE_DELETED, _('Deleted')),
)


class MusicHit(models.Model):
    """ User audio story to be shared with others """
    
    state = models.TextField(
        choices=PUB_STATES,
        default=PUB_STATE_ACTIVE
    )
    
    audio = AudioFileField()
    
    title = models.CharField(max_length=50)
    author = models.ForeignKey("BaseUser", related_name="hit_stories", on_delete=models.CASCADE)
    cover = models.ImageField(upload_to=settings.AUDIO_COVERS_FOLDER)
    publish_date = models.DateTimeField(null=True)