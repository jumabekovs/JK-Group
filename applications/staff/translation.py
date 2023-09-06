from modeltranslation.translator import register, TranslationOptions
from .models import Team


@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'experience', 'status')
