from django.contrib import admin
from .models import Mail


class MailAdmin(admin.ModelAdmin):
    model = Mail
    list_display = ['name', 'email', 'phone_number']
    list_filter = ['email']


# admin.site.register(Mail, MailAdmin)
