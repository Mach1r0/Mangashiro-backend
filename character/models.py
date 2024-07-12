from django.db import models
from anime.models import Anime

class Character(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.CharField(max_length=400)
    anime = models.ForeignKey(Anime, verbose_name="anime", on_delete=models.CASCADE)
