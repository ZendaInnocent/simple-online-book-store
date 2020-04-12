from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'passowrd')}),
        (
            'Personal info',
            {'fields': ('name', )},
        ),
    )
    ordering = ('email', )
    filter_horizontal = ()
    search_fields = ('email', 'name', )
    list_filter = ('is_superuser', )
    list_display = ('email',
                    'name',
                    'is_staff', )


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.unregister(Group)
