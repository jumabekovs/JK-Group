from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Vacancy, CV


class VacancyAdmin(TranslationAdmin):
    model = Vacancy
    list_display = ('title',)


admin.site.register(CV)
admin.site.register(Vacancy, VacancyAdmin)
