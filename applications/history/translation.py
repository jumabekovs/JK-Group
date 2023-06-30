from modeltranslation.translator import register, TranslationOptions
from .models import History, ExtraFields


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'description')


@register(ExtraFields)
class ExtraFieldsTranslationOptions(TranslationOptions):
    fields = ('sub_title', 'description')
