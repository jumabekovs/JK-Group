from django.contrib import admin
from django_summernote.utils import get_attachment_model

from .models import Main
from django.contrib.auth.models import Group, User
from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin


class MainAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = Main
    list_display = ['title', 'subtitle']
    summernote_fields = ('subtitle', 'description', 'text')


admin.site.register(Main, MainAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(get_attachment_model())