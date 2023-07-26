from django.db import models

from applications.company.models import Company
from applications.line.models import Line


class TeamPage(models.Model):
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='team_images',
                                     blank=True, null=True)
    corporate_structure_picture = models.ImageField(verbose_name='фотография структуры', upload_to='team_images',
                                                    blank=True, null=True)

    def __str__(self):
        return "ФОТО КОМАНДЫ и ФОТО СТРУКТУРЫ КОМПАНИИ"

    class Meta:
        verbose_name_plural = "страница команды"


class Team(models.Model):
    company = models.ForeignKey(Company, related_name='teams', on_delete=models.CASCADE, verbose_name='компания',
                             blank=True, null=True)
    line = models.ForeignKey(Line, related_name='lines', on_delete=models.CASCADE, verbose_name='напрвление',
                             blank=True, null=True)
    department = models.CharField(verbose_name="отдел", max_length=255, blank=True, null=True)
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='line_images',
                                     blank=True, null=True)
    name = models.CharField(verbose_name="ФИО", max_length=255)
    status = models.CharField(verbose_name="должность", max_length=255)
    experience = models.TextField(verbose_name='опыт работы')

    def __str__(self):
        return f"{self.company} - {self.department} - {self.name}"

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
