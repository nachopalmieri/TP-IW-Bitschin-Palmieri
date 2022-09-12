

from django.contrib.auth.models import AnonymousUser

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.auth_backends import AuthenticationBackend

from tuneup.utils import cast


class AccountAdapter(DefaultAccountAdapter):
    """ Custom account adapter to configure authentication. """


class AuthBackend(AuthenticationBackend):
    """ Custom auth backend to configure authentication. """
    
    def get_user(self, user_id):
        user = super().get_user(user_id)
        
        if user and user is not AnonymousUser:
            return cast(user)
        
        return user