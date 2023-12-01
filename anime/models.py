from django.db import models
from core.utils import Status
from tag.models import Tag
from staff.models import Staff


class Anime(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=256)
    title_english = models.CharField(max_length=256)
    title_japanese = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/', max_length=255)  # Specify a directory for image uploads
    episodes = models.IntegerField()  # Corrected field name
    release_date = models.DateField()
    status = models.CharField(max_length=256)
    end_date = models.DateField(null=True)
    duration = models.FloatField()  # Corrected field name
    studio = models.TextField(max_length=256)
    tag = models.ManyToManyField(Tag)  # Use the imported Tag model
    status_type = models.TextField(
        max_length=10,
        choices=[(status.value, status.value) for status in Status],
        default=Status.COMPLETED.name,
    )