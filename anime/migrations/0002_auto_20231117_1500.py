# Generated by Django 3.2.12 on 2023-11-17 15:00

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='name',
        ),
        migrations.AddField(
            model_name='anime',
            name='status_type',
            field=models.CharField(choices=[(core.utils.Status['ONHOLD'], 'On Hold'), (core.utils.Status['FINISHED'], 'Finished'), (core.utils.Status['COMPLETED'], 'Completed'), (core.utils.Status['CANCELLED'], 'Cancelled')], default='COMPLETED', max_length=10),
        ),
        migrations.AlterField(
            model_name='anime',
            name='status',
            field=models.CharField(max_length=256),
        ),
    ]
