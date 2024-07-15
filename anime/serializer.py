from rest_framework import serializers
from anime.models import Anime

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'

        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }
