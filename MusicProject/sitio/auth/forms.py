
from django.core.exceptions import ValidationError
from allauth.account.forms import LoginForm as AuthForm

from tuneup.services import verify_user_authorization

class LoginForm(AuthForm):

    def login(self, request, *args, **kwargs):
        
        user = super().login(request, *args, **kwargs)
        
        for error_code, error_msg in verify_user_authorization(request.user):
            raise ValidationError(error_code, error_msg)
        