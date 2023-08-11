from django.contrib import admin
from .models import Company, CompanyImage
from modeltranslation.admin import TranslationAdmin


class CompanyImageAdmin(admin.TabularInline):
    model = CompanyImage
    max_num = 6
    extra = 2


class CompanyAdmin(TranslationAdmin):
    model = Company
    inlines = [CompanyImageAdmin]
    list_display = ['name', 'subtitle']


admin.site.register(Company, CompanyAdmin)
