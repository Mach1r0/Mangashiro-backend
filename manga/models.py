from django.db import models
from enum import Enum
from core.utils import Status

# Create your models here.
class Manga(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(max_length=256)
    releaseData = models.DateField()
    endData = models.DateField()
    Description = models.TextField(max_length=256)
    tag = models.ManyToManyField('Tag')
    staff = models.ManyToManyField('Staff')
    Status = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in Status],
        default=Status.COMPLETED.name,
    )
    