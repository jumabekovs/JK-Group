from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import Vacancy, CV


class VacancyAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = Vacancy
    list_display = ('company', 'title',)
    summernote_fields = ('title', 'description',)


admin.site.register(CV)
admin.site.register(Vacancy, VacancyAdmin)
