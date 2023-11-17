from django.shortcuts import render
from django.views import View
from anime.models import Anime
from anime.serializer import AnimeSerializer
import django.core.exceptions as exceptions 
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.
class UserView(viewsets.ViewSet):
    def create(self, request):
        Anime = UserSerializer(data={
            'email': request.data.get('email',None),
            'password': str(password.hexdigest())
        })

        if user.is_valid(raise_exception=True):
            user.save()
            return Response(user.data, status=201)
        else:
            return Response(user.errors, status=400)

