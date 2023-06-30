from modeltranslation.translator import register, TranslationOptions
from .models import Team


@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('department', 'name', 'experience', 'status')
