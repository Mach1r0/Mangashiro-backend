from django.db import models
from anime.models import Anime# Create your models here.
class Studio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome: models.TextField(max_length=256)
    anime = models.ManyToManyField('anime.Anime')
    manga = models.ManyToManyField('manga.Manga')
    staff = models.ManyToManyField('staff.Staff')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='studios')
