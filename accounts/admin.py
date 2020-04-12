from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email' 'name', )

admin.site.register(CustomUser)

admin.site.unregister(Group)
