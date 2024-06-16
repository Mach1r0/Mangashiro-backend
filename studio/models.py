from django.db import models
from anime.models import Anime
from manga.models import Manga
from staff.models import Staff

class Studio(models.Model):
    nome = models.CharField(max_length=256)
    anime = models.ForeignKey(Anime, verbose_name=("Anime"), on_delete=models.CASCADE, related_name='studios')
    manga = models.ForeignKey(Manga, verbose_name=("Manga"), on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, verbose_name=("Staff"), on_delete=models.CASCADE)