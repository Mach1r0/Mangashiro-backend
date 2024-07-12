# Generated by Django 3.2.12 on 2024-07-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_remove_tag_description'),
        ('studio', '0001_initial'),
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='status',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='studio',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='title_english',
        ),
        migrations.AddField(
            model_name='anime',
            name='Source',
            field=models.CharField(choices=[('manga', 'manga'), ('Night lovel', 'Night lovel')], default='default_value', max_length=100),
        ),
        migrations.AddField(
            model_name='anime',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='anime/'),
        ),
        migrations.AddField(
            model_name='anime',
            name='studios',
            field=models.ManyToManyField(to='studio.Studio', verbose_name='studios'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='anime',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='anime',
            name='tag',
        ),
        migrations.AddField(
            model_name='anime',
            name='tag',
            field=models.ManyToManyField(to='tag.Tag', verbose_name='Tag'),
        ),
    ]