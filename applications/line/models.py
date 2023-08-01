from django.db import models
from applications.company.models import Company


class Line(models.Model):
    company = models.ForeignKey(Company, related_name='lines', on_delete=models.CASCADE, verbose_name='компания')
    title = models.CharField(verbose_name='название', max_length=556)
    sub_title = models.CharField(max_length=999)
    description = models.TextField(verbose_name='описание')
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='line_images',
                                     blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "направление"
        verbose_name_plural = "направления"


class ExtraFields(models.Model):
    line = models.ForeignKey(Line, related_name='extrafields', on_delete=models.CASCADE, verbose_name='направление')
    sub_title = models.CharField(verbose_name='подзаголовок', max_length=999, blank=True, null=True)
    description = models.TextField(verbose_name='описание', blank=True, null=True)
    picture = models.ImageField(verbose_name='первая фотография', upload_to='line_images',
                                blank=True, null=True)
    second_picture = models.ImageField(verbose_name='вторая фотография', upload_to='line_images',
                                       blank=True, null=True)

    def __str__(self):
        return f"{self.sub_title}"

    class Meta:
        verbose_name = 'экстра поле'
        verbose_name_plural = 'экстра поля'
