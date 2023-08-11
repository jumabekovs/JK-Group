from django.db import models

from applications.company.models import Company


class PartnerPage(models.Model):
    sub_title = models.CharField(verbose_name="подзаголовок", max_length=996)
    description = models.TextField(verbose_name='описание')
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='line_images',
                                     blank=True, null=True, max_length=999)
    picture_other = models.ImageField(verbose_name='доп. фотография', upload_to='line_images',
                                      blank=True, null=True, max_length=999)

    def __str__(self):
        return f"{self.sub_title}"

    class Meta:
        verbose_name = "страница партнеров"
        verbose_name_plural = "страница партнеров"


class Partner(models.Model):
    title = models.CharField(verbose_name="заголовок", max_length=556)
    main_picture = models.ImageField(verbose_name='главная фотография 250х250px', upload_to='line_images',
                                     blank=True, null=True, max_length=999)
    picture_other = models.ImageField(verbose_name='доп. фотография 250х250px', upload_to='line_images',
                                      blank=True, null=True, max_length=999)
    description = models.TextField(verbose_name='описание', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "партнер"
        verbose_name_plural = "партнеры"
