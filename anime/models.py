from django.db import models
from django.utils import timezone
from tag.models import Tag

class Anime(models.Model):
    Status_choice = [
        ('Paused', 'On Hold'),
        ('FINISHED', "Finished"),
        ('COMPLETED', "Completed"),
        ('CANCELLED', "Cancelled")
    ]

    title = models.CharField(max_length=256)
    title_english = models.CharField(max_length=256)
    title_japanese = models.CharField(max_length=256)
    episodes = models.IntegerField(default=0)
    release_date = models.DateField(default=timezone.now)  
    status = models.CharField(max_length=256)
    end_date = models.DateField(null=True)
    slug = models.CharField(unique=True, null=False, blank=False, max_length=50)
    duration = models.FloatField(default=0.0)
    studio = models.CharField(max_length=256)
    tag = models.ForeignKey(Tag, verbose_name="Tag", on_delete=models.CASCADE)
    status_type = models.CharField(choices=Status_choice, max_length=40, default='COMPLETED')