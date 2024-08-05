from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializer import (
    UserSerializer,
    ReviewMangaSerializer,
    ReviewAnimeSerializer,
)
from django.http import JsonResponse
from django.contrib.auth import authenticate
from .models import User, ReviewAnime, ReviewManga
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
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
import logging
import os
from django.conf import settings

logger = logging.getLogger(__name__)
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'slug'


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

class Login(APIView):
    def post(self, request):
        nickname = request.data.get('nickname')
        password = request.data.get('password')

        if not nickname or not password:
            logger.error('Nickname and password are required.')
            raise AuthenticationFailed('Nickname and password are required.')

        logger.info(f'Attempting to authenticate user with nickname: {nickname}')
        user = authenticate(request, nickname=nickname, password=password)

        if user is None:
            logger.error(f'Invalid credentials for nickname: {nickname}')
            raise AuthenticationFailed('Invalid credentials.')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1),
            'iat': datetime.datetime.now(datetime.timezone.utc)
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        response = JsonResponse({'message': 'Login successful'})
        response.set_cookie(
            key='accessToken',
            value=token,
            httponly=True,
            max_age=24*60*60,  
            samesite='Strict'
        )
        return response

class UserCount(APIView):
    def get(self, request):
        user_count = User.objects.count()

        data = {
            'user_count' : user_count, 
        },

        return Response(data)
    
