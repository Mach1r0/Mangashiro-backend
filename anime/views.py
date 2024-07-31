from rest_framework import viewsets
from django.http import JsonResponse
from anime.models import Anime
from anime.serializer import AnimeSerializer
from rest_framework.response import Response
from django.db.models import Avg
from rest_framework import status

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

def Anime_count(request):
    Anime_count = Anime.objects.count(); 

    data  = {
        'Anime_count': Anime_count,
    }

    return JsonResponse(data); 

def get_top_5_highest_rated_anime():
    anime_highest_rate = Anime.objects.annotate(avg_rating=Avg('reviewanime__rating'))
    top_5_highest_rated_anime = anime_highest_rate.order_by('-avg_rating')[:10]
    return top_5_highest_rated_anime

class HighestRatedAnimeView(viewsets.ViewSet):
    def list(self, request):
        top_anime = get_top_5_highest_rated_anime()
        if top_anime.exists():
            serializer = AnimeSerializer(top_anime, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No anime found"}, status=status.HTTP_404_NOT_FOUND)