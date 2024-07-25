from rest_framework import serializers
from user.models import User, ReviewAnime, ReviewManga, AnimeState, MangaState

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ReviewMangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewManga
        fields = '__all__'

class ReviewAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewAnime
        fields = '__all__'

class AnimeStatesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AnimeState
        fields = '__all__'

class MangaStateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MangaState
        fields = '__all__'

