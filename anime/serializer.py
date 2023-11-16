from rest_framework import serializers
from anime.models import Anime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'