from django.db import models

from applications.company.models import Company


class History(models.Model):
    title = models.CharField(verbose_name="заголовок", max_length=556)
    title_other = models.CharField(verbose_name="заголовок", max_length=556, blank=True, null=True)
    sub_title = models.CharField(verbose_name="подзаголовок", max_length=996, blank=True, null=True)
    description = models.TextField(verbose_name='описание')
    description_other = models.TextField(verbose_name='описание', null=True, blank=True)
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='history_images',
                                     blank=True, null=True, max_length=999)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "история"
        verbose_name_plural = "история"


class ExtraFields(models.Model):
    history = models.ForeignKey(History, related_name='extrafields', on_delete=models.DO_NOTHING, null=True)
    picture = models.ImageField(verbose_name='фотография', upload_to='history_images',
                                blank=True, null=True, max_length=999)

    def __str__(self):
        return f"{self.history}"

    class Meta:
        verbose_name = 'Экстра картинки'
        verbose_name_plural = 'Экстра картинки'
