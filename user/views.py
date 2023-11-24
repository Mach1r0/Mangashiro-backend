from django.shortcuts import render
from django.views import View
from anime.models import Anime
from anime.serializer import AnimeSerializer
from django.contrib.auth.hashers import make_password
import django.core.exceptions as exceptions 
from rest_framework.response import Response
from rest_framework import viewsets
from django.views.decorators.http import require_http_methods
from user.serializer import UserSerializer  # replace 'your_app_name' with the name of your app

# Create your views here.
class UserView(viewsets.ViewSet):
    @require_http_methods(["POST"])
    def create(self, request):
        user_serializer = UserSerializer(data={
            'email': request.data.get('email',None),
            'password': make_password(request.data.get('password', ''))
        })

        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response(user_serializer.data, status=201)
        else:
            return Response(user_serializer.errors, status=400)