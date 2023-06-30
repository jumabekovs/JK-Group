# Generated by Django 4.2 on 2023-06-30 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_description_alter_company_subtitle_and_more'),
        ('partner', '0003_remove_partner_line_partner_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='company.company', verbose_name='компания'),
        ),
    ]