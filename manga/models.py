from django.db import models
from enum import Enum
from core.utils import Status

# Create your models here.


class Manga(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=256)
    releaseData = models.DateField(null=True)
    endData = models.DateField()
    Description = models.TextField(max_length=256)
    # Assuming 'tag_app' is the name of your tag app
    tag = models.ManyToManyField('tag.Tag')
    # Assuming 'staff_app' is the name of your staff app
    staff = models.ManyToManyField('staff.Staff')
    status_type = models.TextField(  # Renamed 'status' to 'status_type'
        max_length=10,
        choices=[(status.value, status.value) for status in Status],
        default=Status.COMPLETED.name,
    )
