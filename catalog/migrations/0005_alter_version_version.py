# Generated by Django 5.0.4 on 2024-06-10 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_version_current_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version',
            field=models.CharField(verbose_name='Версия'),
        ),
    ]
