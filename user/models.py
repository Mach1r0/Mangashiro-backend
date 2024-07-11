from django.db import models
from anime.models import Anime

class User(models.Model):
    name = models.CharField(unique=True,blank=False, null=False,  max_length=100)
    nickname = models.CharField(max_length=256, null=True,)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    anime =  models.ManyToManyField(Anime, max_length=400)
    description = models.CharField(max_length=400)
    description_image = models.ImageField(upload_to='description/', blank=True, null=True)
    
    def __str__(self):
        return self.name