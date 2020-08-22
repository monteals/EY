"""Emails admin class"""

# Django
from django.contrib import admin

# Models
from emails.models import Emails

@admin.register(Emails)
class EmailsAdmin(admin.ModelAdmin):
    """Email admin"""

    list_display = ('pk', 'user', 'email', 'priority')
    list_display_links = ('pk', 'user',)
    list_editable = ('email',)
    search_fields = ('user__firstname', 'user__last_name', 'email',)


