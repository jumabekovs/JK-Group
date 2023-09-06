from django.db import models

from applications.line.models import Line


class Vacancy(models.Model):
    title = models.CharField(verbose_name="заголовок", max_length=556)
    job = models.CharField(verbose_name="должность", max_length=255, blank=True, null=True)
    line = models.ForeignKey(Line, verbose_name="направление", on_delete=models.SET_NULL, null=True,
                             related_name='vacancy_line')
    description = models.TextField(verbose_name='описание', blank=True, null=True)
    # main_picture = models.ImageField(verbose_name='главная фотография', upload_to='line_images',
    #                                  blank=True, null=True, max_length=999)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'


class CV(models.Model):
    vacancy = models.ForeignKey(Vacancy, related_name='cvs', on_delete=models.CASCADE, verbose_name='вакансия',
                                blank=True, null=True)
    cv = models.FileField(verbose_name="Резюме", upload_to='cv_files')

    def __str__(self):
        return f"{self.cv}"

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
