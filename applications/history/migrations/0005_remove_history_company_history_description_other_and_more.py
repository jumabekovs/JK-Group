# Generated by Django 4.2 on 2023-08-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_alter_extrafields_picture_alter_history_main_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='company',
        ),
        migrations.AddField(
            model_name='history',
            name='description_other',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='history',
            name='title_other',
            field=models.CharField(blank=True, max_length=556, null=True, verbose_name='заголовок'),
        ),
    ]
