from django.db import models

from applications.company.models import Company


class History(models.Model):
    company = models.ForeignKey(Company, verbose_name='компания', related_name='history', on_delete=models.DO_NOTHING,
                                null=True, blank=True)
    title = models.CharField(verbose_name="заголовок", max_length=556)
    sub_title = models.CharField(verbose_name="подзаголовок", max_length=996, blank=True, null=True)
    description = models.TextField(verbose_name='описание')
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='history_images',
                                     blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "история"
        verbose_name_plural = "история"


class ExtraFields(models.Model):
    history = models.ForeignKey(History, related_name='extrafields', on_delete=models.DO_NOTHING, null=True)
    picture = models.ImageField(verbose_name='фотография', upload_to='history_images',
                                blank=True, null=True)

    def __str__(self):
        return f"{self.history}"

    class Meta:
        verbose_name = 'Экстра картинки'
        verbose_name_plural = 'Экстра картинки'

