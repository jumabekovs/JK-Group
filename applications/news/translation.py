from modeltranslation.translator import register, TranslationOptions
from .models import Post, PostCategory


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(PostCategory)
class PostTranslationOptions(TranslationOptions):
    fields = ('name', )
