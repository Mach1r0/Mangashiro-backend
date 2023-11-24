from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from user.serializer import UserSerializer  # replace 'user' with the name of your app
from user.models import User  # replace 'user' with the name of your app

class UserView(APIView):
    def CreateUser(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            user.password = make_password(user.password)
            user.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def telalogin(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
            'refresh': str(refresh),
            'acess': str(refresh.acess_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'erro': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)