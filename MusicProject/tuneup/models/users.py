
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractUser,
    UserManager as DefaultManager
)
from django.core.exceptions import ValidationError


USER_STATE_ACTIVE = 'ACTIVE'
USER_STATE_ACTIVE_UNVERIFIED = 'ACTIVE_UNVERIFIED'
USER_STATE_SUSPENDED = 'SUSPENDED'
USER_STATE_BLOQUED = 'BLOQUED'
USER_STATE_DELETED = 'DELETED'

USER_STATES = (
    (USER_STATE_ACTIVE, _('Active')),
    (USER_STATE_ACTIVE_UNVERIFIED, _('Active (Unverified)')),
    (USER_STATE_SUSPENDED, _('Suspended')),
    (USER_STATE_BLOQUED, _('Bloqued')),
    (USER_STATE_DELETED, _('Deleted'))
)


def user_factory(is_superuser=False):
    
    if is_superuser:
        return AdminUser
    
    return StandardUser


class UserManager(DefaultManager):
    
    def _create_user(self, username, email, password, **extra_fields):    
        
        if self.model is BaseUser:
        
            is_superuser = extra_fields.get('is_superuser')
            
            if is_superuser:
                extra_fields.setdefault('state', USER_STATE_ACTIVE)
            
            model = user_factory(is_superuser=is_superuser)
            
            return model.objects._create_user(username, email, password, **extra_fields)
        
        return super()._create_user(username, email, password, **extra_fields)


class BaseUser(AbstractUser):
    """ Base user class with common fields and features for all users types. """
    
    objects = UserManager()
    
    state = models.TextField(
        choices=USER_STATES,
        default=USER_STATE_ACTIVE_UNVERIFIED
    )
    
    # States from where the user can be active again.
    activable_states = (
        USER_STATE_ACTIVE_UNVERIFIED,
        USER_STATE_SUSPENDED
    )
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("All Users") 
    
    def assign_default_permissions(self):
        """ Set permissions and related fields for user. """
        self.is_staff = False
        self.is_superuser = False 
    
    def activate(self):
        """ Makes an user active. """
        
        if self.state not in self.activable_states:
            raise ValidationError(
                f"User can't be re-actvated from state '{ self.state }'"
            )
        
        self.state = USER_STATE_ACTIVE
        self.save()
    
    def save(self, *args, **kwargs):
        
        self.is_active = self.state is not USER_STATE_DELETED
        
        self.assign_default_permissions()
        
        super().save(*args, **kwargs)


class AdminUser(BaseUser):
    """ Users from staff related to our administration. """
    
    class Meta(BaseUser.Meta):
        verbose_name = _("Admin User")
        verbose_name_plural = _("Admin Users")
    
    def assign_default_permissions(self):
        self.is_staff = True
        self.is_superuser = True 


class StandardUser(BaseUser):
    """ Users with access to common apps features and standard usage. """
    
    class Meta(BaseUser.Meta):
        verbose_name = _("Standard User")
        verbose_name_plural = _("Standard Users")