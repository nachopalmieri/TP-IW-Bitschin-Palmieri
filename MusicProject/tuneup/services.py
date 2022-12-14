
from django.dispatch import Signal
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from tuneup.models.users import (
    # User States
    USER_STATE_ACTIVE,
    USER_STATE_ACTIVE_UNVERIFIED,
    USER_STATE_SUSPENDED,
    USER_STATE_BLOQUED,
)
from tuneup.models.publications import PUB_STATE_ACTIVE
from tuneup.repositories import get_hits


on_new_hit_published = Signal()


def create_user(user):
    """ Creates a new user for platform backend. """
    
    if user.is_superuser:
        # Admin users must be created as verified.
        user.state = USER_STATE_ACTIVE
    
    user.save()


def publish_new_hit(music_hit):
    """ Publishes a new audio hit. """

    if music_hit.publish_date:
        raise ValueError("This hit is already published.")
    
    if not music_hit.audio.is_valid:
        raise ValueError(f"Invalid or unsupported audio file '{ music_hit.audio.extension }'")

    music_hit.publish_date = timezone.now()
    music_hit.save()

    on_new_hit_published.send(sender=publish_new_hit, music_hit=music_hit)


def get_feed_for_user(user):
    """ Gets user personal feed. """
    
    return get_hits(
        state=PUB_STATE_ACTIVE,
        ordering=['-publish_date']
    )


def get_user_authorization_errors(user):
    """ Checks user authorization on the platform,
    returns a list with all auth errors. """
    
    forbiden_states = {
        USER_STATE_ACTIVE_UNVERIFIED: (
            "inactive",
            _("Check your email and use verification link for first login.")
        ),
        USER_STATE_BLOQUED: (
            "inactive_bloqued",
            _("Your account has been permanently bloqued by an administrator.")
        ),
        USER_STATE_SUSPENDED: (
            "inactive_suspended",
            _("Your account has been temporaly suspended by an administrator.")
        ),
    }
    
    error = forbiden_states.get(user.state)
    
    if not error:
        # User allowed in platforms
        return []
    
    return [error]