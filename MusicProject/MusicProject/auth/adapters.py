
from django.core.exceptions import ValidationError

from allauth.utils import get_user_model
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from tuneup.models import StandardUser
from tuneup.services import get_user_authorization_errors, create_user


class AccountAdapter(DefaultAccountAdapter):
    """ Custom account adapter to configure authentication. """

    def new_user(self, request):
        return StandardUser()
    
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        create_user(user)
    
    def confirm_email(self, request, email_address):
        super().confirm_email(request, email_address)
        
        try:
            email_address.user.activate()
        except ValidationError:
            pass
        
    def authenticate(self, request, **credentials):
        
        user = super().authenticate(request, **credentials)
        
        if user:
            
            auth_errors = get_user_authorization_errors(user)
            
            if auth_errors:
                code, error = auth_errors[0]
                raise ValidationError(error, code)
        
        return user


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    """ Custom social account adapter to configure authentication. """

    def new_user(self, request):
        return StandardUser()