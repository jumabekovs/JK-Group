from django.contrib import admin
from .models import Career, CareerImages
from modeltranslation.admin import TranslationAdmin


class CareerImagesAdmin(admin.TabularInline):
    model = CareerImages
    max_num = 6
    extra = 1


class CareerAdmin(TranslationAdmin):
    model = Career
    inlines = [CareerImagesAdmin]
    list_display = ['title']


admin.site.register(Career, CareerAdmin)
