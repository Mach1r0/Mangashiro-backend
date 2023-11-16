from rest_framework import viewsets
from rest_framework.response import Response
from anime.models import Anime
from anime.serializers import AnimeSerializer

class AnimeViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving animes.
    """
    def list(self, request):
        queryset = Anime.objects.all()
        serializer = AnimeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Anime.objects.all()
        anime = get_object_or_404(queryset, pk=pk)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)