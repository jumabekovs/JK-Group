from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import Post


class PostAdmin(SummernoteModelAdmin, TranslationAdmin):
    model = Post
    list_display = ['title', 'content']
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
