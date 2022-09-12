""" Module to handle data access queries or operations. """

from tuneup.models.publications import MusicHit


def get_hits_feed(user=None):
    """ Gets hit stories. """
    
    filters = {}
    
    if user is not None:
        filters['user'] = user
    
    return (MusicHit.objects
                .filter(is_active=True, **filters)
                .order_by('-publish_date'))