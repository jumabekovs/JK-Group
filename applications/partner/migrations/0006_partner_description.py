# Generated by Django 4.2 on 2023-07-20 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0005_partner_title_en_partner_title_ky_partner_title_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
    ]