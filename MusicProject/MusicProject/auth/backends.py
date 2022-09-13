
from allauth.account.auth_backends import AuthenticationBackend


class AuthBackend(AuthenticationBackend):
    """ Custom auth backend to configure authentication. """