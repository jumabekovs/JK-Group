from django.contrib import admin
from .models import Mission, ExtraFields
from modeltranslation.admin import TranslationAdmin


class ExtraFieldsAdmin(admin.TabularInline):
    model = ExtraFields
    max_num = 3
    extra = 1


class MissionAdmin(TranslationAdmin):
    model = Mission
    inlines = [ExtraFieldsAdmin]
    list_display = ['title', 'sub_title']


admin.site.register(Mission, MissionAdmin)
