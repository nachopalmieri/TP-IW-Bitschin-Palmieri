

def is_verified_email(email_model, email: str):
    """ Checks if an `email` has been verified. """
    return email_model.objects.filter(
        email=email, verified=True
    ).exists()


def get_hits_feed(hits_model, user=None):
    """ Gets hit stories. """
    
    filters = {}
    
    if user is not None:
        filters['user'] = user
    
    return (hits_model.objects
                .filter(is_active=True, **filters)
                .order_by('-publish_date'))