from django.db import models

from applications.company.models import Company


class Vacancy(models.Model):
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE, verbose_name='компания',
                                blank=True, null=True)
    title = models.CharField(verbose_name="заголовок", max_length=556)
    description = models.TextField(verbose_name='описание')
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='line_images',
                                     blank=True, null=True)

    def __str__(self):
        return f"{self.company} - {self.title}"

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'