from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import Team, TeamPage


class TeamAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = Team
    list_display = ('company', 'department', 'name', 'status')
    summernote_fields = ('experience',)


admin.site.register(Team, TeamAdmin)
admin.site.register(TeamPage)
