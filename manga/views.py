from rest_framework import viewsets
from manga.models import Manga
from manga.serializer import MangaSerializer
from rest_framework.response import Response

class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

def get_top_5_highest_rated_manga():
    manga_highest_rate = Manga.objects.annotate(avg_rating=Avg('reviewmanga__rating'))
    top_5_highest_rated_manga = manga_highest_rate.order_by('-avg_rating')[:10]
    return top_5_highest_rated_manga

class HighestRatedMangaView(viewsets.ViewSet):
    def list(self, request):
        top_manga = get_top_5_highest_rated_manga()
        if top_manga.exists():
            serializer = MangaSerializer(top_manga, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No manga found"}, status=status.HTTP_404_NOT_FOUND)