""" Module to handle data access queries or operations. """

from tuneup.models.publications import MusicHit


def get_hits(ordering=[], **filters):
    """ Gets hit stories. """
    
    return (MusicHit.objects
                .filter(**filters)
                .order_by(*ordering))