from django.db import models

from applications.company.models import Company


class PartnerPage(models.Model):
    sub_title = models.CharField(verbose_name="подзаголовок", max_length=996)
    description = models.TextField(verbose_name='описание')
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='line_images',
                                     blank=True, null=True, max_length=999)

    def __str__(self):
        return f"{self.sub_title}"

    class Meta:
        verbose_name = "страница партнеров"
        verbose_name_plural = "страница партнеров"


class Partner(models.Model):
    company = models.ForeignKey(Company, related_name='partners_company', on_delete=models.CASCADE, verbose_name='компания')
    title = models.CharField(verbose_name="заголовок", max_length=556)
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='line_images',
                                     blank=True, null=True, max_length=999)
    description = models.TextField(verbose_name='описание', blank=True, null=True)

    def __str__(self):
        return f"{self.company.name} - {self.title}"

    class Meta:
        verbose_name = "партнер"
        verbose_name_plural = "партнеры"
