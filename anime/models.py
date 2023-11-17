from django.db import models
from core.utils import Status

class Anime(models.Model):
    name = models.CharField(max_length=256)
    release_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    tag = models.ManyToManyField('Tag')
    staff = models.ManyToManyField('Staff')
    status = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in Status],
        default=Status.COMPLETED.name,
    )