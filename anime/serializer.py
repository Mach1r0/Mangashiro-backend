from rest_framework import serializers
from anime.models import Anime

class AnimeSerializer(serializers.ModelSerializer):
    studios = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    slug = serializers.SlugRelatedField(
        slug_field='title',
        read_only=True
    )

    class Meta:
        model = Anime
        fields = [
            'title', 'title_japanese', 'episodes', 'release_date', 'end_date', 
            'duration', 'studios', 'Source', 'tag', 'image', 'Background', 'slug'
        ]
        extra_kwargs = {
            'Source': {'default': 'default_value'}
        }
