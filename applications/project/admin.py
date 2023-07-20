from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import Project


class ProjectAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = Project
    list_display = ['title', 'year', ]
    list_display_links = ['title', 'year', ]
    summernote_fields = ('title', 'description')


admin.site.register(Project,ProjectAdmin)
