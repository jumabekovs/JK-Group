# Generated by Django 4.2 on 2023-08-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_mail_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Подзаголовок')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'обратная связь',
                'verbose_name_plural': 'обратная связь',
            },
        ),
    ]
