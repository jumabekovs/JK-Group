from modeltranslation.translator import register, TranslationOptions
from .models import Post, PostCategory


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'content', 'description')


@register(PostCategory)
class PostTranslationOptions(TranslationOptions):
    fields = ('name',)
