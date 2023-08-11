from django.db import models


class PostCategory(models.Model):
    name = models.CharField(verbose_name='название', max_length=256)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Post(models.Model):
    category = models.ForeignKey(PostCategory, verbose_name='категория', related_name='post_categories',
                                 on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(verbose_name='название', max_length=256, unique=True)
    sub_title = models.CharField(verbose_name='подзоголовок', max_length=256, blank=True, null=True)
    content = models.TextField(verbose_name='контент', blank=True, null=True)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    image = models.ImageField(verbose_name='картинка 1800х830px', upload_to='post_images', blank=True, null=True, max_length=999)

    def __str__(self):
        return f"{self.category}"

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
