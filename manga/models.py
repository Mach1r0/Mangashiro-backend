from django.db import models
from tag.models import Tag 

class Manga(models.Model):
    Status_choice = [
        ('Paused', 'On Hold'),
        ("FINISHED",  "Finished"),
        ("COMPLETED",  "Completed"),
        ("CANCELLED",  "Cancelled")
    ]

    title = models.CharField(max_length=256)  
    description = models.CharField(max_length=5000)
    chapters = models.IntegerField(default=1)  
    volume = models.IntegerField()
    tag = models.ManyToManyField(Tag, related_name='tag')  
    release_date = models.DateField(null=True)  
    end_date = models.DateField() 
    image = models.ImageField(upload_to='anime-img', null=True, blank=True)  
    background = models.ImageField(upload_to='anime-background-img', null=True, blank=True)  
    status_type = models.CharField(choices=Status_choice, max_length=30)

    def __str__(self) -> str:
        return self.title