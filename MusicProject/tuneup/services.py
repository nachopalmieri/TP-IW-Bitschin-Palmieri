
from django.utils import timezone
from django.dispatch import Signal


on_new_hit_published = Signal()


def publish_new_hit(music_hit):
    """ Publishes a new audio hit. """

    if music_hit.publish_date:
        raise ValueError("This hit is already published.")

    music_hit.publish_date = timezone.now()
    music_hit.save()

    on_new_hit_published.send(music_hit=music_hit)