from django.db import models
from django.utils.text import slugify
from tag.models import Tag 
from django.utils import timezone

class Manga(models.Model):
    Status_choice = [
        ('Paused', 'On Hold'),
        ("FINISHED",  "Finished"),
        ("COMPLETED",  "Completed"),
        ("CANCELLED",  "Cancelled")
    ]

    title = models.CharField(max_length=256, unique=True)  
    description = models.CharField(max_length=5000)
    chapters = models.IntegerField(default=1)  
    volume = models.IntegerField()
    tag = models.ManyToManyField(Tag, related_name='tag')  
    release_date = models.DateField(blank=True, null=True, default=timezone.now)
    end_date = models.DateField(blank=True, null=True, default=timezone.now)
    image = models.ImageField(upload_to='anime-img', null=True, blank=True)  
    background = models.ImageField(upload_to='anime-background-img', null=True, blank=True)  
    status_type = models.CharField(choices=Status_choice, max_length=30)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
