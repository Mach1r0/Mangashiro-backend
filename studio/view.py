from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudioSerializer

class StudioView(viewsets.ViewSet):
    def create(self, request):
        serializer = StudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)