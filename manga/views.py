from rest_framework import viewsets
from manga.models import Manga
from manga.serializer import MangaSerializer

class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer