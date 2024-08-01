from rest_framework import serializers
from user.models import User, ReviewAnime, ReviewManga
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    manga_states = serializers.JSONField(required=False)
    anime_states = serializers.JSONField(required=False)

    class Meta:
        model = User
        fields = ['name', 'nickname', 'password', 'email', 'background', 'image_profile', 'description', 'description_image', 'manga_states', 'anime_states']
        extra_kwargs = {
            'password': {'write_only': True},
            'manga_states': {'read_only': True},  
            'anime_states': {'read_only': True},  
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            nickname=validated_data['nickname'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class ReviewMangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewManga
        fields = '__all__'

class ReviewAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewAnime
        fields = '__all__'

