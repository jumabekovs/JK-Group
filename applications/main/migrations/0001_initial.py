# Generated by Django 4.2 on 2023-07-25 07:33

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='название')),
                ('title_ru', models.CharField(max_length=256, null=True, unique=True, verbose_name='название')),
                ('title_ky', models.CharField(max_length=256, null=True, unique=True, verbose_name='название')),
                ('title_en', models.CharField(max_length=256, null=True, unique=True, verbose_name='название')),
                ('description', models.TextField(default='Комплексный инжиниринг в Кыргызской Республике', verbose_name='лозунг')),
                ('description_ru', models.TextField(default='Комплексный инжиниринг в Кыргызской Республике', null=True, verbose_name='лозунг')),
                ('description_ky', models.TextField(default='Комплексный инжиниринг в Кыргызской Республике', null=True, verbose_name='лозунг')),
                ('description_en', models.TextField(default='Комплексный инжиниринг в Кыргызской Республике', null=True, verbose_name='лозунг')),
                ('main_video', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='видео')),
                ('subtitle', models.CharField(blank=True, max_length=556, null=True, verbose_name='подзоголовок')),
                ('subtitle_ru', models.CharField(blank=True, max_length=556, null=True, verbose_name='подзоголовок')),
                ('subtitle_ky', models.CharField(blank=True, max_length=556, null=True, verbose_name='подзоголовок')),
                ('subtitle_en', models.CharField(blank=True, max_length=556, null=True, verbose_name='подзоголовок')),
                ('text', models.TextField(blank=True, null=True, verbose_name='текст')),
                ('text_ru', models.TextField(blank=True, null=True, verbose_name='текст')),
                ('text_ky', models.TextField(blank=True, null=True, verbose_name='текст')),
                ('text_en', models.TextField(blank=True, null=True, verbose_name='текст')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
    ]
