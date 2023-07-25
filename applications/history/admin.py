from django.contrib import admin
from .models import History, ExtraFields
from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin


class ExtraFieldsAdmin(SummernoteModelAdminMixin, admin.TabularInline):
    model = ExtraFields
    max_num = 6
    extra = 1


class HistoryAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = History
    inlines = [ExtraFieldsAdmin]
    list_display = ['company', 'title', 'sub_title']
    summernote_fields = ('sub_title', 'description')


admin.site.register(History, HistoryAdmin)
