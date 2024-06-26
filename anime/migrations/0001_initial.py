# Generated by Django 3.2.12 on 2024-06-15 22:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('title_english', models.CharField(max_length=256)),
                ('title_japanese', models.CharField(max_length=256)),
                ('episodes', models.IntegerField(default=0)),
                ('release_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=256)),
                ('end_date', models.DateField(null=True)),
                ('slug', models.CharField(max_length=50, unique=True)),
                ('duration', models.FloatField(default=0.0)),
                ('studio', models.CharField(max_length=256)),
                ('status_type', models.CharField(choices=[('Paused', 'On Hold'), ('FINISHED', 'Finished'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='COMPLETED', max_length=40)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.tag', verbose_name='Tag')),
            ],
        ),
    ]
