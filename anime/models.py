from django.db import models
from core.utils import Status
from tag.models import Tag
from staff.models import Staff
#class tag(Tag):
 #   serializer = super()

class Anime(models.Model):
    id = models.BigAutoField(primary_key=true)
    name = models.CharField(max_length=256)
    release_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    tag = models.ManyToManyField('tag.Tag')  # Assuming 'tag_app' is the name of your tag app
    staff = models.ManyToManyField('staff.Staff')  # Assuming 'staff_app' is the name of your staff app
    status = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in Status],
        default=Status.COMPLETED.name,
    )