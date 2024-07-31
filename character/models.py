from django.db import models
from anime.models import Anime
from manga.models import Manga

class Character(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    image = models.ImageField(upload_to='character-img', null=True, blank=True)
    anime = models.ForeignKey(Anime, verbose_name="anime", on_delete=models.CASCADE, null=True, blank=True)
    manga = models.ForeignKey(Manga, verbose_name="manga", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    