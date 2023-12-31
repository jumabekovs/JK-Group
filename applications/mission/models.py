from django.db import models

from applications.company.models import Company


class Mission(models.Model):
    title = models.CharField(verbose_name="заголовок", max_length=556)
    sub_title = models.CharField(verbose_name="подзаголовок", max_length=996)
    description = models.TextField(verbose_name='описание')
    main_picture = models.ImageField(verbose_name='фотография 2000x840p', upload_to='line_images',
                                     blank=True, null=True, max_length=999)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "миссия"
        verbose_name_plural = "миссии"


class ExtraFields(models.Model):
    mission = models.ForeignKey(Mission, related_name='extrafields', on_delete=models.CASCADE, verbose_name='направление')
    sub_title = models.CharField(verbose_name="подзаголовок", max_length=999, blank=True, null=True)
    description = models.TextField(verbose_name='описание', blank=True, null=True)
    picture = models.ImageField(verbose_name='фотография миссии 350х420px', upload_to='mission_images',
                                blank=True, null=True)

    def __str__(self):
        return f"{self.sub_title}"

    class Meta:
        verbose_name = 'подробная информация'
        verbose_name_plural = 'подробная информация'

