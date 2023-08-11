from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Project, ExtraFields


class ExtraFieldsAdmin(admin.TabularInline):
    model = ExtraFields
    max_num = 3
    extra = 1


class ProjectAdmin(TranslationAdmin):
    model = Project
    inlines = [ExtraFieldsAdmin]
    list_display = ['title', 'year', ]
    list_display_links = ['title', 'year', ]


admin.site.register(Project, ProjectAdmin)
