# Generated by Django 3.2.12 on 2024-07-11 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='type',
        ),
    ]
