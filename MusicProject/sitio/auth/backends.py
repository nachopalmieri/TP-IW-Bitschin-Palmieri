
from allauth.account.auth_backends import AuthenticationBackend

from tuneup.models.users import get_user_from_base


class SiteAuthBackend(AuthenticationBackend):
    
    def authenticate(self, request, **credentials):
        
        user = super().authenticate(request, **credentials)
        
        if user:
            
            return get_user_from_base(user)
        
        return user