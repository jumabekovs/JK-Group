# Generated by Django 4.2 on 2023-06-29 15:41

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0002_alter_company_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=556, verbose_name='название')),
                ('sub_title', models.CharField(max_length=999)),
                ('description', models.TextField(verbose_name='описание')),
                ('main_picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='company.company', verbose_name='компания')),
            ],
            options={
                'verbose_name': 'направление',
                'verbose_name_plural': 'направления',
            },
        ),
        migrations.CreateModel(
            name='ExtraFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=999)),
                ('description', models.TextField(verbose_name='описание')),
                ('picture', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extrafields', to='line.line', verbose_name='направление')),
            ],
            options={
                'verbose_name': 'экстра поле',
                'verbose_name_plural': 'экстра поля',
            },
        ),
    ]
