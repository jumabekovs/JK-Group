# Generated by Django 4.2 on 2023-06-30 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_description_alter_company_subtitle_and_more'),
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='line',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='company.company', verbose_name='компания'),
        ),
    ]
