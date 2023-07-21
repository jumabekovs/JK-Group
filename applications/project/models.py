from django.db import models
from applications.line.models import Line


class Project(models.Model):
    line = models.ForeignKey(Line, related_name='projects', on_delete=models.CASCADE, verbose_name='направление')
    title = models.CharField(verbose_name='название', max_length=265)
    description = models.TextField(verbose_name='описание')
    file = models.ImageField(verbose_name='фотография', upload_to='project_images',
                                     blank=True, null=True)
    year = models.IntegerField(verbose_name='год', blank=True, null=True)

    def __str__(self):
        return f"{self.line} - {self.title}"

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'


class ExtraFields(models.Model):
    line = models.ForeignKey(Project, related_name='extrafields', on_delete=models.CASCADE, verbose_name='проект')
    picture = models.ImageField(verbose_name='фотография проекта', upload_to='line_images',
                                blank=True, null=True)

    class Meta:
        verbose_name = 'экстра поле'
        verbose_name_plural = 'экстра поля'
