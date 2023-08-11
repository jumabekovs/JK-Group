from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import PartnerPage, Partner


class PartnerAdmin(TranslationAdmin):
    model = Partner
    list_display = ['title', ]


class PartnerPageAdmin(TranslationAdmin):
    model = PartnerPage
    list_display = ['sub_title',]


admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerPage, PartnerPageAdmin)
