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
        ('Night lovel', 'Night lovel')
    ]

    image = models.ImageField(upload_to='anime/', null=True, blank=True)  
    title = models.CharField(max_length=256)
    title_japanese = models.CharField(max_length=256)
    episodes = models.IntegerField(default=0)
    release_date = models.DateField(default=timezone.now)  
    end_date = models.DateField(null=True, blank=True)
    slug = models.CharField(unique=True, null=False, blank=False, max_length=50)
    duration = models.IntegerField(default=0)
    studios = models.ManyToManyField(Studio, verbose_name="studios")  
    Source = models.CharField(choices=Source_choice, max_length=100, default='default_value')
    tag = models.ManyToManyField(Tag, verbose_name="Tag")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Run migrations for related apps
        from django.core.management import call_command
        call_command('makemigrations', 'anime')
        call_command('makemigrations', 'studio')
    status_type = models.CharField(choices=Status_choice, max_length=40, default='COMPLETED')