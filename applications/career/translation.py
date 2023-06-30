from modeltranslation.translator import register, TranslationOptions
from .models import Career


@register(Career)
class CareerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
