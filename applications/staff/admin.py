from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Team, TeamPage, Department


class TeamAdmin(TranslationAdmin):
    model = Team
    list_display = ('line', 'department', 'name', 'status')


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ("line",)


admin.site.register(Team, TeamAdmin)
admin.site.register(TeamPage)
admin.site.register(Department, DepartmentAdmin)
