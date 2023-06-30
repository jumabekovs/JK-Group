from modeltranslation.translator import register, TranslationOptions
from .models import Line, ExtraFields


@register(Line)
class LineTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'description')


@register(ExtraFields)
class ExtraFieldsTranslationOptions(TranslationOptions):
    fields = ('sub_title', 'description')