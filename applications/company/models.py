from django.db import models

from applications.main.models import Main


class Company(models.Model):
    name = models.CharField(verbose_name="название", max_length=256)
    group = models.ForeignKey(Main, related_name='companies', on_delete=models.CASCADE)
    subtitle = models.CharField(verbose_name="подзаголовок", max_length=999)
    description = models.TextField()
