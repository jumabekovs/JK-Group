from django.db import models
from applications.line.models import Line


class Project(models.Model):
    line = models.ForeignKey(Line, related_name='projects', on_delete=models.CASCADE, verbose_name='направление')
    title = models.CharField(verbose_name='название', max_length=265)
    sub_title = models.CharField(verbose_name='подзоголовок', max_length=265, blank=True, null=True)
    description = models.TextField(verbose_name='описание')
    description_other = models.TextField(verbose_name='доп. описание', blank=True, null=True)
    picture = models.ImageField(verbose_name='фотография слева', upload_to='project_images',
                                blank=True, null=True, max_length=999)
    picture_other = models.ImageField(verbose_name='фотография справа  300x720px', upload_to='project_images',
                                      blank=True, null=True, max_length=999)
    year = models.IntegerField(verbose_name='год', blank=True, null=True)

    def __str__(self):
        return f"{self.line} - {self.title}"

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'


class ExtraFields(models.Model):
    line = models.ForeignKey(Project, related_name='extrafields', on_delete=models.CASCADE, verbose_name='проект')
    picture = models.ImageField(verbose_name='доп.фотографии для карусели', upload_to='line_images 350х420px',
                                blank=True, null=True, max_length=999)

    class Meta:
        verbose_name = 'подробная информация'
        verbose_name_plural = 'подробная информация'
