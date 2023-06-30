# Generated by Django 4.2 on 2023-06-30 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('line', '0003_alter_extrafields_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=556, verbose_name='заголовок')),
                ('description', models.TextField(verbose_name='описание')),
                ('main_picture', models.ImageField(blank=True, null=True, upload_to='line_images', verbose_name='главная фотография')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='line.line', verbose_name='направление')),
            ],
            options={
                'verbose_name': 'вакансия',
                'verbose_name_plural': 'вакансии',
            },
        ),
    ]