# Generated by Django 4.2 on 2023-08-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyimage',
            name='image',
            field=models.ImageField(blank=True, max_length=999, null=True, upload_to='company-images', verbose_name='фотография'),
        ),
    ]
