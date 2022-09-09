from django.contrib import admin

from tuneup.models import BaseUser, AdminUser, StandardUser

admin.site.register(BaseUser)
admin.site.register(AdminUser)
admin.site.register(StandardUser)