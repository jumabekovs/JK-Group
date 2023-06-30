from django.db import models

from applications.main.models import Main


class Company(models.Model):
    name = models.CharField(verbose_name="название", max_length=256)
    group = models.ForeignKey(Main, related_name='companies', on_delete=models.CASCADE)
    subtitle = models.CharField(verbose_name="подзаголовок", max_length=999, blank=True, null=True)
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class CompanyImage(models.Model):
    company = models.ForeignKey(Company, related_name='company_images', on_delete=models.CASCADE,
                                verbose_name='компания')
    image = models.ImageField(verbose_name='фотография', upload_to='company-images', blank=True, null=True)

    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
