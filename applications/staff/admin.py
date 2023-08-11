from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Team, TeamPage


class TeamAdmin(TranslationAdmin):
    model = Team
    list_display = ('line', 'department', 'name', 'status')


admin.site.register(Team, TeamAdmin)
admin.site.register(TeamPage)
