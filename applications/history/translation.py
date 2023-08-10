from modeltranslation.translator import register, TranslationOptions
from .models import History, ExtraFields


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'description', 'title_other', 'description_other')
