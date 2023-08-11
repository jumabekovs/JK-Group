from django.contrib import admin
from .models import AboutUs
from modeltranslation.admin import TranslationAdmin


class AboutUsAdmin(TranslationAdmin):
    model = AboutUs
    list_display = ['title', 'subtitle']


admin.site.register(AboutUs, AboutUsAdmin)

