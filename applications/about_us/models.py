from django.db import models


class AboutUs(models.Model):
    title = models.CharField(verbose_name='название', max_length=256, unique=True)
    subtitle = models.CharField(verbose_name='подзоголовок', max_length=556, blank=True, null=True)
    subtitle_other = models.CharField(verbose_name='подзоголовок', max_length=556, blank=True, null=True)
    description = models.TextField(verbose_name='текст')
    description_other = models.TextField(verbose_name='текст', blank=True, null=True)
    picture = models.ImageField(verbose_name='фотография 2000x840px', upload_to='about_us_image',
                                blank=True, null=True, max_length=999)

    def __str__(self):
        return f"{self.title} - {self.description}"

    class Meta:
        verbose_name = "Cтраница о нас"
        verbose_name_plural = "Cтраница о нас"
