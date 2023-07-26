from django.contrib import admin
from .models import AboutUs
from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin


class AboutUsAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = AboutUs
    list_display = ['title', 'subtitle']
    summernote_fields = ('description', )


admin.site.register(AboutUs, AboutUsAdmin)

