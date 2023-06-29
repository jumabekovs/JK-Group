# Generated by Django 4.2 on 2023-06-29 14:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='main',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главная страница'},
        ),
        migrations.AlterField(
            model_name='main',
            name='main_video',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='видео главной страница'),
        ),
    ]