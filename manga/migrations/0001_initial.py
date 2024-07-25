# Generated by Django 3.2.12 on 2024-07-25 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=5000)),
                ('chapters', models.IntegerField(default=1)),
                ('volume', models.IntegerField()),
                ('release_date', models.DateField(null=True)),
                ('end_date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='anime-img')),
                ('background', models.ImageField(blank=True, null=True, upload_to='anime-background-img')),
                ('status_type', models.CharField(choices=[('Paused', 'On Hold'), ('FINISHED', 'Finished'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], max_length=30)),
                ('tag', models.ManyToManyField(related_name='tag', to='tag.Tag')),
            ],
        ),
    ]
