from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import PartnerPage, Partner


class PartnerAdmin(TranslationAdmin):
    model = Partner
    list_display = ['title', ]


class PartnerPageAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = PartnerPage
    list_display = ['description', 'sub_title']
    summernote_fields = ('description',)


admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerPage, PartnerPageAdmin)
