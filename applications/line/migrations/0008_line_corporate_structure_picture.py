# Generated by Django 4.2 on 2023-09-06 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line', '0007_alter_extrafields_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='corporate_structure_picture',
            field=models.ImageField(blank=True, null=True, upload_to='line_images', verbose_name='фотография структуры 2000x840px'),
        ),
    ]
