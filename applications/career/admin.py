from django.contrib import admin
from .models import Career, CareerImages
from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin


class CareerImagesAdmin(admin.TabularInline):
    model = CareerImages
    max_num = 6
    extra = 1


class CareerAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = Career
    inlines = [CareerImagesAdmin]
    summernote_fields = ('description')
    list_display = ['title']


admin.site.register(Career, CareerAdmin)
