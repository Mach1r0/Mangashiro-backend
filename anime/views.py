from rest_framework import viewsets
from anime.models import Anime
from anime.serializer import  AnimeSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer