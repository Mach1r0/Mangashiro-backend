from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }