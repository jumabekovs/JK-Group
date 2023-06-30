from django.contrib import admin
from .models import Mission, ExtraFields
from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin


class ExtraFieldsAdmin(SummernoteModelAdminMixin, admin.TabularInline):
    model = ExtraFields
    max_num = 6
    extra = 1
    summernote_fields = ('sub_title_ru', 'sub_title_ky', 'sub_title_en', 'description_ru', 'description_ky',
                         'description_en',)
    exclude = ('sub_title', 'description')


class MissionAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = Mission
    inlines = [ExtraFieldsAdmin]
    list_display = ['company', 'title', 'sub_title']
    summernote_fields = ('title', 'sub_title', 'description')


admin.site.register(Mission, MissionAdmin)
