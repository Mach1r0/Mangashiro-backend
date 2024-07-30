from rest_framework import serializers
from user.models import User, ReviewAnime, ReviewManga, AnimeState, MangaState

from rest_framework import serializers
from user.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'nickname', 'password', 'email', 'background', 'image_profile', 'description', 'description_image']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            nickname=validated_data['nickname'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



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

