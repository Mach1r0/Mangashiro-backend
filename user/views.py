# views.py
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializer import (
    UserSerializer,
    ReviewMangaSerializer,
    ReviewAnimeSerializer,
    AnimeStateSerializer,
    MangaStateSerializer,
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
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

class AnimeStateViewSet(viewsets.ModelViewSet):
    queryset = AnimeState.objects.all()
    serializer_class = AnimeStateSerializer

class MangaStateViewSet(viewsets.ModelViewSet):
    queryset = MangaState.objects.all()
    serializer_class = MangaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReviewMangaListView(ListAPIView):
    serializer_class = ReviewMangaSerializer
    paginate_by = 5

    def get_queryset(self):
        nickname = self.kwargs.get('nickname')
        user = get_object_or_404(User, nickname=nickname)
        return ReviewManga.objects.filter(user=user).order_by('-date_posted')

class ReviewAnimeListView(ListAPIView):
    serializer_class = ReviewAnimeSerializer
    paginate_by = 5

    def get_queryset(self):
        nickname = self.kwargs.get('nickname')
        user = get_object_or_404(User, nickname=nickname)
        return ReviewAnime.objects.filter(user=user).order_by('-date_posted')

class UserReviewMangaView(ListAPIView):
    serializer_class = ReviewMangaSerializer

    def get_queryset(self):
        user = get_object_or_404(User, nickname=self.kwargs.get('nickname'))
        return ReviewManga.objects.filter(user=user)

class UserReviewAnimeView(ListAPIView):
    serializer_class = ReviewAnimeSerializer

    def get_queryset(self):
        user = get_object_or_404(User, nickname=self.kwargs.get('nickname'))
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

class Register(APIView):
    def post(self, request): 
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import jwt
from django.contrib.auth import get_user_model
import datetime
from django.contrib.auth.hashers import check_password
import logging

logger = logging.getLogger(__name__)

User = get_user_model()

class Login(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            logger.error('gmail and password are required.')
            raise AuthenticationFailed('Nickname and password are required.')

        # Log the attempt to fetch user
        logger.info(f'Attempting to find user with email: {email}')
        user = User.objects.filter(email=email).first()

        if user is None:
            logger.error(f'User not found with email: {email}')
            raise AuthenticationFailed('User not found!')

        if not check_password(password, user.password):
            logger.error(f'Incorrect password for email: {email}')
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
