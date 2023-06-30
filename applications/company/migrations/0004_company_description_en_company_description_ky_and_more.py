# Generated by Django 4.2 on 2023-06-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_description_alter_company_subtitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description_en',
            field=models.TextField(null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='company',
            name='description_ky',
            field=models.TextField(null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='company',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='описание'),
        ),
    ]