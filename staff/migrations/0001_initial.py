# Generated by Django 3.2.12 on 2023-11-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=256)),
                ('desenhista', models.CharField(max_length=256, null=True)),
                ('assistente', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
