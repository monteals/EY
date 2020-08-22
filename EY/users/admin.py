"""User admin class"""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""

    list_display = ('pk', 'user', 'first_name', 'first_last_name', 'second_last_name')
    list_display_links = ('pk', 'user')
    list_editable = ('first_name', 'first_last_name', 'second_last_name')
    search_fields = ('user__email', 'user__firstname', 'user__first_last_name', 'user__second_last_name',)

class ProfileInline (admin.StackedInline):
    """Profile in-line admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""

    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
