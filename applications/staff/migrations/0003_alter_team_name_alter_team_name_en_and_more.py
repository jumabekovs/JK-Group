# Generated by Django 4.2 on 2023-07-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_team_department_alter_team_department_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=255, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='ФИО'),
        ),
    ]
