# Generated by Django 3.2.12 on 2024-07-21 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0005_alter_anime_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='Background',
            field=models.ImageField(blank=True, null=True, upload_to='static/anime-background-img/'),
        ),
    ]