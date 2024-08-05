# Generated by Django 3.2.12 on 2024-08-02 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manga', '0001_initial'),
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='manga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manga.manga', verbose_name='manga'),
        ),
    ]