from rest_framework import viewsets
from anime.models import Anime
from anime.serializer import  AnimeSerializer
from django.http import JsonResponse

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

def Anime_count(request):
    Anime_count = Anime.objects.count(); 

    data  = {
        'Anime_count': Anime_count,
    }

    return JsonResponse(data); 

