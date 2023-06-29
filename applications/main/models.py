from django.db import models
from cloudinary.models import CloudinaryField


class Main(models.Model):
    title = models.CharField(verbose_name='название', max_length=256, unique=True)
    description = models.TextField(verbose_name='лозунг', default="Комплексный инжиниринг в Кыргызской Республике")
    main_video = CloudinaryField(resource_type="video", verbose_name='видео главной страница', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"
