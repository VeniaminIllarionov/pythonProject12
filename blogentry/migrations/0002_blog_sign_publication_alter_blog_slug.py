# Generated by Django 5.0.4 on 2024-05-20 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogentry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sign_publication',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Slug'),
        ),
    ]
