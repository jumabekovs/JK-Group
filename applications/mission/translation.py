from modeltranslation.translator import register, TranslationOptions
from .models import Mission, ExtraFields


@register(Mission)
class MissionTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'description')


@register(ExtraFields)
class ExtraFieldsTranslationOptions(TranslationOptions):
    fields = ('sub_title', 'description')