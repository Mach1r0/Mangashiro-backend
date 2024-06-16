from rest_framework import viewsets
from studio.models import Studio
from studio.serializer import StudioSerializer

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
