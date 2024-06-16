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
    slug = models.CharField(max_length=256, unique=True, blank=False, null=False)
    type = models.CharField(max_length=256)  
    volume = models.IntegerField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tag')  
    release_date = models.DateField(null=True)  
    end_date = models.DateField() 
    image = models.ImageField(upload_to='manga/', null=True, blank=True)  
    status_type = models.CharField(choices=Status_choice, max_length=30)