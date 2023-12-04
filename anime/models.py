from django.db import models
from core.utils import Status
from tag.models import Tag
from staff.models import Staff

class Anime(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256)
    title_english = models.CharField(max_length=256)
    title_japanese = models.CharField(max_length=256)
    episodes = models.IntegerField(default='0')
    release_date = models.DateField(default='0-0-0')
    status = models.CharField(max_length=256)
    end_date = models.DateField(null=True)
    duration = models.FloatField(default='0')
    studio = models.CharField(max_length=256)  # Changed from TextField to CharField
    tag = models.ManyToManyField(Tag)
    status_type = models.CharField(  # Changed from TextField to CharField
        max_length=10,
        choices=[(status.value, status.value) for status in Status],
        default=Status.COMPLETED.name,
    )