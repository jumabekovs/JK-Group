from django.db import models

from applications.company.models import Company
from applications.line.models import Line


class TeamPage(models.Model):
    main_picture = models.ImageField(verbose_name='главная фотография 2000x840px', upload_to='team_images',
                                     blank=True, null=True)
    corporate_structure_picture = models.ImageField(verbose_name='фотография структуры 2000x840px', upload_to='team_images',
                                                    blank=True, null=True)

    def __str__(self):
        return "ФОТО КОМАНДЫ и ФОТО СТРУКТУРЫ КОМПАНИИ"

    class Meta:
        verbose_name_plural = "страница команды"


class Department(models.Model):
    line = models.ForeignKey(Line, related_name='department_lines', on_delete=models.CASCADE, verbose_name='напрвление',
                             blank=True, null=True)
    name = models.CharField(verbose_name="отдел", max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="описание", blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "отдел"
        verbose_name_plural = "отделы"


class Team(models.Model):
    line = models.ForeignKey(Line, related_name='team_lines', on_delete=models.CASCADE, verbose_name='напрвление',
                             blank=True, null=True)
    department = models.ForeignKey(Department, verbose_name="отдел", related_name="team_department",
                                   on_delete=models.SET_NULL, null=True, blank=True)
    main_picture = models.ImageField(verbose_name='фотография 390x500px', upload_to='line_images',
                                     blank=True, null=True, max_length=500)
    name = models.CharField(verbose_name="ФИО", max_length=255)
    status = models.CharField(verbose_name="должность", max_length=255)
    experience = models.TextField(verbose_name='опыт работы')

    def __str__(self):
        return f"{self.department} - {self.name}"

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'

