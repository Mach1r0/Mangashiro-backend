from django.contrib.auth.hashers import make_password
import django.core.exceptions as exceptions
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from user.serializer import UserSerializer  # replace 'user' with the name of your app
from user.models import User  # replace 'user' with the name of your app
import hashlib


class UserView(viewsets.ViewSet):
    # Method for user registration
    def create(self, request):
        # Create a UserSerializer with the request data
        user_serializer = UserSerializer(data=request.data)
        
        # Validate the data
        if user_serializer.is_valid():
            # If the data is valid, create a User instance
            user = user_serializer.save()
            # Hash the user's password and save the user again
            user.password = hashlib.sha256(request.data.get('password', None).encode('utf-8'))
            user.password = str(user.password.hexdigest())
            user.save()
            # Create a JWT refresh token for the user
            refresh = RefreshToken.for_user(user)
            # Return the refresh and access tokens in the response
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        else:
            # If the data is not valid, return the errors in the response
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Method for user login
    def login(self, request):
        try:
            login_email = request.data.get('email', None)
            user = User.objects.get(email=login_email)
        # Authenticate the user
            password = hashlib.sha256(request.data.get('password', None).encode())
            print (password)
            print (user.password)
            if password.hexdigest() == user.password:
                print("gets here")
        # If the user is authenticated, create a JWT refresh token for the user
                refresh = RefreshToken.for_user(user)
            # Return the refresh and access tokens in the response
                return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
            # If the user is not authenticated, return an error in the response
                return Response({'error': 'Invalid Credentials password does not match',
                                 "password" : user.password}, status=status.HTTP_400_BAD_REQUEST)
        except (User.DoesNotExist, exceptions.FielError):
            print("none here")
            return Response({'error': 'Invalid Credentials user does not exist'}, status=status.HTTP_400_BAD_REQUEST)