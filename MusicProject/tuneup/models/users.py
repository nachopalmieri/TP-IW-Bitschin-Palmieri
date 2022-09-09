
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractUser,
    UserManager
)

from allauth.account.models import EmailAddress

from tuneup.repository import is_verified_email
from tuneup.models.mixins.publications import PublishHitMixin, FeedHitMixin


USER_STATE_ACTIVE = 'ACTIVE'
USER_STATE_SUSPENDED = 'SUSPENDED'
USER_STATE_BLOQUED = 'BLOQUED'

USER_STATES = (
    (USER_STATE_ACTIVE, _('Active')),
    (USER_STATE_SUSPENDED, _('Suspended')),
    (USER_STATE_BLOQUED, _('Bloqued'))
)


def user_factory(is_superuser=False):
    
    if is_superuser:
        return AdminUser
    
    return StandardUser


def get_user_from_base(base_user_instance):
    user_refs = ['admin_user', 'standard_user']
    
    for ref in user_refs:
        
        user = getattr(base_user_instance, ref, None)
        
        if user:
            
            return user


class StandardUserManager(UserManager):
    """ Manager class for general user management features. """
    
    def _create_user(self, username, email, password, **extra_fields):
        
        is_superuser = extra_fields.get('is_superuser', False)
        
        return (user_factory(is_superuser=is_superuser).objects
                    ._create_user(username, email, password, **extra_fields))


class BaseUser(AbstractUser, FeedHitMixin):
    """ Base user class with common fields and features for all users types. """
    
    objects = StandardUserManager()
    
    state = models.TextField(choices=USER_STATES, default=USER_STATE_ACTIVE)
    
    def assign_default_permissions(self, fields: dict):
        """ Set permissions and fields related before saving. """
        raise NotImplementedError
    
    @property
    def is_verified(self):
        return is_verified_email(EmailAddress, self.email)
    
    def save(self, *args, **kwargs):
        
        self.is_active = self.state is USER_STATE_ACTIVE
        
        self.assign_default_permissions(kwargs)
        
        super().save(*args, **kwargs)


class AdminUser(BaseUser):
    """ Users from staff related to our administration. """
    
    def assign_default_permissions(self, fields: dict):
        
        self.is_staff = True
        self.is_superuser = True

        fields['is_staff'] = self.is_staff
        fields['is_superuser'] = self.is_superuser


class StandardUser(BaseUser, PublishHitMixin):
    """ Users with access to common apps features and standard usage. """
    
    def assign_default_permissions(self, fields: dict): 
        
        self.is_staff = False
        self.is_superuser = False
        
        fields['is_staff'] = self.is_staff
        fields['is_superuser'] = self.is_superuser