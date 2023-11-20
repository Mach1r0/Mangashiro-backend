from django.db import models
from core.utils import Status
from tag.models import Tag
from staff.models import Staff

class Anime(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=256)  # Replaced 'name' with 'status'
    release_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    tag = models.ManyToManyField('tag.Tag')  # Assuming 'tag_app' is the name of your tag app
    staff = models.ManyToManyField('staff.Staff')  # Assuming 'staff_app' is the name of your staff app
    status_type = models.TextField(  # Renamed 'status' to 'status_type'
        max_length=10,
        choices=[(status.value, status.value) for status in Status],
        default=Status.COMPLETED.name,
    )
