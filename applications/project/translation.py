from modeltranslation.translator import register, TranslationOptions
from .models import Project


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'description', 'description_other')
