# Generated by Django 4.2 on 2023-08-14 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_post_description_en_post_description_ky_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(blank=True, max_length=999, null=True, upload_to='line_images', verbose_name='фотография')),
            ],
            options={
                'verbose_name': 'фотография новостей',
                'verbose_name_plural': 'фотография новостей',
            },
        ),
    ]