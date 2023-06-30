from django.db import models

from applications.line.models import Line


class Vacancy(models.Model):
    line = models.ForeignKey(Line, related_name='vacancies', on_delete=models.CASCADE, verbose_name='направление')
    title = models.CharField(verbose_name="заголовок", max_length=556)
    description = models.TextField(verbose_name='описание')
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='line_images',
                                     blank=True, null=True)

    def __str__(self):
        return f"{self.line} - {self.title}"

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
