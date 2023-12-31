# Generated by Django 4.2 on 2023-07-25 07:33

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_picture', models.ImageField(blank=True, null=True, upload_to='line_images', verbose_name='главная фотография')),
                ('main_video', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='видео')),
                ('title', models.CharField(max_length=556, verbose_name='заголовок')),
                ('title_ru', models.CharField(max_length=556, null=True, verbose_name='заголовок')),
                ('title_ky', models.CharField(max_length=556, null=True, verbose_name='заголовок')),
                ('title_en', models.CharField(max_length=556, null=True, verbose_name='заголовок')),
                ('description', models.TextField(verbose_name='описание')),
                ('description_ru', models.TextField(null=True, verbose_name='описание')),
                ('description_ky', models.TextField(null=True, verbose_name='описание')),
                ('description_en', models.TextField(null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'карьера',
                'verbose_name_plural': 'карьера',
            },
        ),
        migrations.CreateModel(
            name='CareerImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='career_images', verbose_name='фотография')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='career.career', verbose_name='карьера')),
            ],
            options={
                'verbose_name': 'экстра поле',
                'verbose_name_plural': 'экстра поля',
            },
        ),
    ]
