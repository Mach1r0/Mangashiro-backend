from django.db import models
from enum import Enum
from core.utils import Status

# Create your models here.


class Manga(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(max_length=256)
    type = models.TextField(max_length=256)
    volume = models.IntegerField()
    tag = models.ManyToManyField('tag.Tag')
    releaseData = models.DateField(null=True)
    endData = models.DateField()
    models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    status_type = models.TextField(  # Renamed 'status' to 'status_type'
        max_length=10,
        choices=[(status.value, status.value) for status in Status],
        default=Status.COMPLETED.name,
    )
