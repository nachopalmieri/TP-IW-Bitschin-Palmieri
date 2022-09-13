
from django.contrib.auth import logout
from django.utils.functional import SimpleLazyObject
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.middleware import AuthenticationMiddleware, get_user
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages

from tuneup.utils import cast
from tuneup.services import get_user_authorization_errors


def get_casted_user(request):
    user = get_user(request)
    
    if user and user.is_authenticated:
        return cast(user)
    
    return user


class AuthMiddleware(AuthenticationMiddleware):
    
    def process_request(self, request):
        if not hasattr(request, "session"):
            raise ImproperlyConfigured(
                "The Django authentication middleware requires session "
                "middleware to be installed. Edit your MIDDLEWARE setting to "
                "insert "
                "'django.contrib.sessions.middleware.SessionMiddleware' before "
                "'django.contrib.auth.middleware.AuthenticationMiddleware'."
            )
        request.user = SimpleLazyObject(lambda: get_casted_user(request))
        
        if request.user and not request.user.is_anonymous:
            
            errors = get_user_authorization_errors(request.user)
            
            if errors:
                storage = messages.get_messages(request)
                storage.used = True
            
            for code, error in errors:
                messages.error(request, error)
            
            if errors:
                logout(request)
                return redirect(settings.LOGIN_URL)