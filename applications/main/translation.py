from modeltranslation.translator import register, TranslationOptions
from .models import Main


@register(Main)
class MainTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'text')
