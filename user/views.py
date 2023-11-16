from django.shortcuts import render
from django.views import View
from user.models import User
from user.serializer import UserSerializer
import hashlib
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.
class UserView(viewsets.ViewSet):
    def create(self, request):
        password = hashlib.sha256(request.data.get('password',None).enconde('utf-8'))
        user = UserSerializer(data={
            'email': request.data.get('email',None),
            'password': str(password.hexdigest())
        })

        if user.is_valid(raise_exeption=True):
            user.save()
            return Response(user.data, status=201)
        else:
            return Response(user.errors, status=400)

