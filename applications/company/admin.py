from django.contrib import admin
from .models import Company, CompanyImage


class CompanyImageAdmin(admin.TabularInline):
    model = CompanyImage
    max_num = 6
    extra = 2


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    inlines = [CompanyImageAdmin]
    list_display = ['name', 'subtitle']


admin.site.register(Company, CompanyAdmin)
