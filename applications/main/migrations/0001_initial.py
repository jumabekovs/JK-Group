# Generated by Django 4.2 on 2023-06-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='название')),
                ('description', models.TextField(default='Комплексный инжиниринг в Кыргызской Республике', verbose_name='лозунг')),
                ('main_video', models.FileField(blank=True, null=True, upload_to='jk-main-video', verbose_name='видео главной страница')),
            ],
        ),
    ]