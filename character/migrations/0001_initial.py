# Generated by Django 3.2.12 on 2024-08-02 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='character-img')),
                ('anime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anime.anime', verbose_name='anime')),
            ],
        ),
    ]
