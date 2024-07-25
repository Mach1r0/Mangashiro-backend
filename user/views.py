# views.py
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializer import (
    UserSerializer,
    ReviewMangaSerializer,
    ReviewAnimeSerializer,
    MangaStateSerializer,
    AnimeStatesSerializer
)
from .models import User, ReviewAnime, ReviewManga, AnimeState, MangaState
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from manga.models import Manga
from anime.models import Anime
from rest_framework.views import APIView
from manga.serializer import MangaSerializer
from anime.serializer import AnimeSerializer
from django.db.models import Avg
from rest_framework import status
from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReviewMangaListView(ListAPIView):
    serializer_class = ReviewMangaSerializer
    paginate_by = 5

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return ReviewManga.objects.filter(user=user).order_by('-date_posted')

class ReviewAnimeListView(ListAPIView):
    serializer_class = ReviewAnimeSerializer
    paginate_by = 5

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return ReviewAnime.objects.filter(user=user).order_by('-date_posted')

class UserReviewMangaView(ListAPIView):
    serializer_class = ReviewMangaSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ReviewManga.objects.filter(user=user)

class UserReviewAnimeView(ListAPIView):
    serializer_class = ReviewAnimeSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ReviewAnime.objects.filter(user=user)

class ReviewMangaViewSet(viewsets.ModelViewSet):
    queryset = ReviewManga.objects.all()
    serializer_class = ReviewMangaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ReviewAnimeViewSet(viewsets.ModelViewSet):
    queryset = ReviewAnime.objects.all()
    serializer_class = ReviewAnimeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

def get_top_5_highest_rated_manga():
    manga_highest_rate = Manga.objects.annotate(avg_rating=Avg('reviewmanga__rating'))
    top_5_highest_rated_manga = manga_highest_rate.order_by('-avg_rating')[:10]
    return top_5_highest_rated_manga

def get_top_5_highest_rated_anime():
    anime_highest_rate = Anime.objects.annotate(avg_rating=Avg('reviewanime__rating'))
    top_5_highest_rated_anime = anime_highest_rate.order_by('-avg_rating')[:10]
    return top_5_highest_rated_anime


class HighestRatedMangaView(viewsets.ViewSet):
    def list(self, request):
        top_manga = get_top_5_highest_rated_manga()
        if top_manga.exists():
            serializer = MangaSerializer(top_manga, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No manga found"}, status=status.HTTP_404_NOT_FOUND)

class HighestRatedAnimeView(viewsets.ViewSet):
    def list(self, request):
        top_anime = get_top_5_highest_rated_anime()
        if top_anime.exists():
            serializer = AnimeSerializer(top_anime, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No anime found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def UserCreate(request): 
    serializers = UserSerializer(data=request.DATA); 
    if serializers.is_valid():
        User.objects.is_valid(
            serializers.init_data['email'], 
            serializers.init_data['username'],
            serializers.init_data['password'], 
        )
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    else: 
        return Response(serializers._errors, status=status.HTTP_400_BAD_REQUEST)