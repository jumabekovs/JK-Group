# Generated by Django 4.2 on 2023-08-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0003_remove_mission_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrafields',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='mission_images', verbose_name='фотография миссии 350х420px'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='main_picture',
            field=models.ImageField(blank=True, max_length=999, null=True, upload_to='line_images', verbose_name='фотография 2000x840p'),
        ),
    ]
