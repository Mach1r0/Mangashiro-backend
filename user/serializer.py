from rest_framework import serializers
from user.models import User, Review, AnimeState, MangaState

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class AnimeStatesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AnimeState
        fields = '__all__'

class MangaStateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MangaState
        fields = '__all__'