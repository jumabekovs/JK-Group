from cloudinary.models import CloudinaryField
from django.db import models


class Career(models.Model):
    main_picture = models.ImageField(verbose_name='главная фотография', upload_to='line_images',
                                     blank=True, null=True)
    main_video = CloudinaryField(resource_type="video", verbose_name='видео 2000х700px', null=True, blank=True)
    title = models.CharField(verbose_name="заголовок", max_length=556)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'карьера'
        verbose_name_plural = 'карьера'


class CareerImages(models.Model):
    career = models.ForeignKey(Career, related_name='images', on_delete=models.CASCADE, verbose_name='карьера')
    picture = models.ImageField(verbose_name='фотография 350х420px', upload_to='career_images',
                                blank=True, null=True)

    class Meta:
        verbose_name = 'экстра поле'
        verbose_name_plural = 'экстра поля'
