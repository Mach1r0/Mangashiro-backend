# Generated by Django 3.2.12 on 2024-07-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0004_alter_anime_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='Source',
            field=models.CharField(choices=[('manga', 'manga'), ('Light novel', 'Light novel'), ('Crunchyroll', 'Crunchyroll'), ('Netflix', 'Netflix')], default='default_value', max_length=100),
        ),
    ]