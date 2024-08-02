from rest_framework import viewsets, generics
from manga.models import Manga
from manga.serializers import MangaSerializer
from rest_framework.response import Response
from django.db.models import Avg
from rest_framework import status

class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    lookup_field = 'slug'

def get_top_10_highest_rated_manga():
    manga_highest_rate = Manga.objects.annotate(avg_rating=Avg('reviews__rating'))
    top_10_highest_rated_manga = manga_highest_rate.order_by('-avg_rating')[:10]
    return top_10_highest_rated_manga

class HighestRatedMangaView(generics.ListAPIView):
    serializer_class = MangaSerializer

    def get_queryset(self):
        return get_top_10_highest_rated_manga()
