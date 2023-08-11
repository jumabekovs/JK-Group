from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Post, PostCategory


class PostCategoryAdmin(TranslationAdmin):
    model = PostCategory
    list_display = ['name', ]


class PostAdmin(TranslationAdmin):
    model = Post
    list_display = ['title', ]


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
