from django.contrib import admin
from django_summernote.utils import get_attachment_model

from .models import Main
from django.contrib.auth.models import Group, User


admin.site.register(Main)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(get_attachment_model())