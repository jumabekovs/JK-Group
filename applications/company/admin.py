from django.contrib import admin
from .models import Company, CompanyImage
from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin


class CompanyImageAdmin(admin.TabularInline):
    model = CompanyImage
    max_num = 6
    extra = 2


class CompanyAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = Company
    inlines = [CompanyImageAdmin]
    list_display = ['name', 'subtitle']
    summernote_fields = ('description',)


admin.site.register(Company, CompanyAdmin)
