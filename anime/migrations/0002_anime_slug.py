# Generated by Django 3.2.12 on 2024-08-02 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
