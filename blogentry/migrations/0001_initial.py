# Generated by Django 5.0.4 on 2024-05-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Описание')),
                ('slug', models.CharField(max_length=150, verbose_name='Slug')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blogentry/photo', verbose_name='Изображение')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
