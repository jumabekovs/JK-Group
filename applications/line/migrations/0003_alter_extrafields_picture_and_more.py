# Generated by Django 4.2 on 2023-08-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line', '0002_extrafields_second_picture_alter_extrafields_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrafields',
            name='picture',
            field=models.ImageField(blank=True, max_length=999, null=True, upload_to='line_images', verbose_name='первая фотография'),
        ),
        migrations.AlterField(
            model_name='extrafields',
            name='second_picture',
            field=models.ImageField(blank=True, max_length=999, null=True, upload_to='line_images', verbose_name='вторая фотография'),
        ),
        migrations.AlterField(
            model_name='line',
            name='main_picture',
            field=models.ImageField(blank=True, max_length=999, null=True, upload_to='line_images', verbose_name='главная фотография'),
        ),
    ]
