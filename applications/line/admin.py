from django.contrib import admin
from .models import Line, ExtraFields
from modeltranslation.admin import TranslationAdmin


class ExtraFieldsAdmin(admin.TabularInline):
    model = ExtraFields
    max_num = 3
    extra = 1


class LineAdmin(TranslationAdmin):
    model = Line
    inlines = [ExtraFieldsAdmin]
    list_display = ['title']


admin.site.register(Line, LineAdmin)
