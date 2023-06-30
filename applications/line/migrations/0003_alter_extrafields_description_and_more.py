# Generated by Django 4.2 on 2023-06-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line', '0002_alter_extrafields_picture_alter_line_main_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrafields',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='extrafields',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='line_images', verbose_name='фотография направление'),
        ),
        migrations.AlterField(
            model_name='extrafields',
            name='sub_title',
            field=models.CharField(blank=True, max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='main_picture',
            field=models.ImageField(blank=True, null=True, upload_to='line_images', verbose_name='главная фотография'),
        ),
    ]
