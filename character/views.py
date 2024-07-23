from rest_framework import viewsets
from .serializer import CharacterSerializer
from .models import Character

class CharacterView(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()