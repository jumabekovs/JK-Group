from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Post, PostCategory, PostPage


class PostCategoryAdmin(TranslationAdmin):
    model = PostCategory
    list_display = ['name', ]


class PostAdmin(TranslationAdmin):
    model = Post
    list_display = ['title', ]


class PostBackground(admin.ModelAdmin):
    model = PostPage
    list_display = ['img_preview', 'background_image']


admin.site.register(Post, PostAdmin)
admin.site.register(PostPage, PostBackground)
admin.site.register(PostCategory, PostCategoryAdmin)
