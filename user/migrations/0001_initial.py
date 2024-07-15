# Generated by Django 3.2.12 on 2024-07-14 02:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manga', '0002_auto_20240713_0314'),
        ('anime', '0003_auto_20240713_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('PLANNING', 'Planning to Watch'), ('COMPLETED', 'Completed'), ('WATCHED', 'Watched'), ('DROPPED', 'Dropped'), ('WATCHING', 'Watching')], max_length=10)),
                ('times_watched', models.PositiveIntegerField(default=1)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime')),
            ],
        ),
        migrations.CreateModel(
            name='MangaState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('PLANNING', 'Planning to Read'), ('COMPLETED', 'Completed'), ('READ', 'Read'), ('DROPPED', 'Dropped'), ('READING', 'Reading')], max_length=10)),
                ('times_read', models.PositiveIntegerField(default=1)),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.manga')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('nickname', models.CharField(max_length=256, null=True)),
                ('password', models.CharField(max_length=256)),
                ('background', models.ImageField(blank=True, null=True, upload_to='background/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='user/')),
                ('email', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=400)),
                ('description_image', models.ImageField(blank=True, null=True, upload_to='description/')),
                ('anime', models.ManyToManyField(related_name='users', through='user.AnimeState', to='anime.Anime')),
                ('manga', models.ManyToManyField(related_name='users', through='user.MangaState', to='manga.Manga')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('Title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('anime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anime.anime')),
                ('manga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manga.manga')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.AddField(
            model_name='mangastate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='animestate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
