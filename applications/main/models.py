from django.db import models


class Main(models.Model):
    title = models.CharField(verbose_name='название', max_length=256, unique=True)
    description = models.TextField(verbose_name='лозунг', default="Комплексный инжиниринг в Кыргызской Республике")
    main_video = models.FileField(blank=True, null=True, verbose_name='видео главной страница', upload_to='jk-main-video')

    def __str__(self):
        return f"{self.title}"
