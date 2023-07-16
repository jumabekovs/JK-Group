from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import Project


class ProjectAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = Project
    list_display = ['name', 'year', ]
    list_display_links = ['name', 'year', ]
    summernote_fields = ('name', 'description')


admin.site.register(Project,ProjectAdmin)
