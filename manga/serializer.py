from rest_framework import serializers
from manga.models import Manga

class MangaSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Manga
        fields = [
            'title', 'description', 'chapters', 'volume', 'tag', 
            'release_date', 'end_date', 'image', 'background', 'status_type', 'slug'
        ]