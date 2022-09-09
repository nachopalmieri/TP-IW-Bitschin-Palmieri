
from django.utils import timezone
from django.dispatch import Signal

from tuneup.repository import get_hits_feed


on_new_hit_published = Signal() 


class PublishHitMixin:
    
    def publish_hit(self, audio_hit):
        """ Publish an audio hit. """
        
        if audio_hit.publish_date:
            raise ValueError("This hit is already published.")

        audio_hit.publish_date = timezone.now()
        
        self.hit_stories.add(audio_hit)
        
        on_new_hit_published.send(sender=self, new_hit=audio_hit)


class FeedHitMixin:
    
    def get_feed(self):
        """ Gets personalized hits feed for user. """
        return get_hits_feed(type(self), user=self)