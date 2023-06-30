from django.db import models
from django.utils.translation import gettext_lazy as _


class NewsCategory(models.TextChoices):
    NEWS_COMPANY = ('Новости компании', _('Новости компании'))
    PRESS_RELEASES = ('Пресс-релизы', _('Пресс-релизы'))
    EVENTS = ('События', _('События'))
    GALLERY = ('Галерея', _('Галерея'))


class Post(models.Model):
    category = models.CharField(verbose_name='категория', max_length=20, choices=NewsCategory.choices,
                                blank=True, null=True)
    title = models.CharField(verbose_name='название', max_length=256, blank=True, null=True)
    content = models.TextField(verbose_name='контент', blank=True, null=True)
    image = models.ImageField(verbose_name='картинка поста', upload_to='post_images', blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.title}"

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
