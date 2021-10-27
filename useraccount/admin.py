from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name', 'date_of_birth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name',
                'last_name',
                'email',
                'date_of_birth',
                'password1',
                'password2'
            ),
        }),
    )
    list_display = (
        'email',
        'first_name',
        'last_name',
        'date_of_birth',
        'is_staff'
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'date_of_birth'
    )
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
