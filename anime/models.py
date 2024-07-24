from studio.models import Studio
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

    Source_choice = [ 
        ('manga', 'manga'), 
        ('Light novel', 'Light novel'),
        ('Crunchyroll', 'Crunchyroll'),
        ('Netflix', 'Netflix'),
    ]

    title = models.CharField(max_length=256)
    title_japanese = models.CharField(max_length=256)
    episodes = models.IntegerField(default=0)
    release_date = models.DateField(default=timezone.now)  
    end_date = models.DateField(null=True, blank=True)
    duration = models.IntegerField(default=0)
    studios = models.ManyToManyField(Studio, verbose_name="studios")  
    Source = models.CharField(choices=Source_choice, max_length=100, default='default_value')
    tag = models.ManyToManyField(Tag, verbose_name="Tag")
    image = models.ImageField(upload_to='anime-img/', null=True, blank=True)  
    Background = models.ImageField(upload_to='anime-background-img/', null=True, blank=True)  
    
    def __str__(self) -> str:
        return self.title; 