from rest_framework import viewsets
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Manga
from .serializer import MangaSerializer

class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    lookup_field = 'slug'

def get_top_10_highest_rated_manga():
    manga_highest_rate = Manga.objects.annotate(avg_rating=Avg('reviews__rating'))
    top_10_highest_rated_manga = manga_highest_rate.order_by('-avg_rating')[:10]
    return top_10_highest_rated_manga

class MangaCountViews(APIView):
    def get(self, request):
        manga_count = Manga.objects.count()
        data = {
            'manga_count': manga_count,
        }
        return Response(data)
    
class HighestRatedMangaView(viewsets.ViewSet):
    def list(self, request):
        top_manga = get_top_10_highest_rated_manga()
        if top_manga.exists():
            serializer = MangaSerializer(top_manga, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No manga found"}, status=status.HTTP_404_NOT_FOUND)
