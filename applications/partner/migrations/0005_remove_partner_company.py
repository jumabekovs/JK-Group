# Generated by Django 4.2 on 2023-08-09 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0004_alter_partner_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='company',
        ),
    ]
