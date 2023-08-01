from modeltranslation.translator import register, TranslationOptions
from .models import Partner, PartnerPage


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(PartnerPage)
class PartnerPageTranslationOptions(TranslationOptions):
    fields = ('sub_title', 'description')
