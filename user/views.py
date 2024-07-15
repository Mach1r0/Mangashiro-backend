from rest_framework import viewsets
from .serializer import UserSerializer, ReviewSerializer, MangaStateSerializer, AnimeStatesSerializer 
from .models import User, Review, AnimeState, MangaState
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, get_object_or_404
from .models import Review, User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewListView(ListAPIView):
    serializer_class = ReviewSerializer
    paginate_by = 5

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return Review.objects.filter(user=user).order_by('-date_posted')


class UserReviewView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'));
        return Review.objects.filter(author=user); 
