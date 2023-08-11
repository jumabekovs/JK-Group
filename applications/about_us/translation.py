from modeltranslation.translator import register, TranslationOptions
from .models import AboutUs


@register(AboutUs)
class MainTranslationOptions(TranslationOptions):
    fields = ('subtitle', 'description', 'subtitle_other', 'description_other',)
