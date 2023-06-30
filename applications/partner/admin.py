from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import PartnerPage, Partner


class PartnerAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = Partner
    list_display = ['title',]
    summernote_fields = ('title', )


class PartnerPageAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = PartnerPage
    list_display = ['description', 'sub_title']
    summernote_fields = ('sub_title', 'description')


admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerPage, PartnerPageAdmin)
