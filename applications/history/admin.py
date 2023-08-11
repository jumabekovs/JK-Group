from django.contrib import admin
from .models import History, ExtraFields
from modeltranslation.admin import TranslationAdmin


class ExtraFieldsAdmin(admin.TabularInline):
    model = ExtraFields
    max_num = 3
    extra = 1


class HistoryAdmin(TranslationAdmin):
    model = History
    inlines = [ExtraFieldsAdmin]
    list_display = ['title', 'sub_title']


admin.site.register(History, HistoryAdmin)
