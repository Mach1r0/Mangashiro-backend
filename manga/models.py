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
    tag = models.ManyToManyField('tag.Tag')  # Assuming 'tag_app' is the name of your tag app
    staff = models.ManyToManyField('staff.Staff')  # Assuming 'staff_app' is the name of your staff app
    Status = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in Status],
        default=Status.COMPLETED.name,
    )
    