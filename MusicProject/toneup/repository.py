from allauth.account.admin import EmailAddress


def is_verified_email(email: str):
    """ Checks if an `email` has been verified. """
    return EmailAddress.objects.filter(
        email=email, verified=True
    ).exists()
