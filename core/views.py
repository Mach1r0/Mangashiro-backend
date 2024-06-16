from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from anime.models import Anime
from manga.models import Manga
from studio.models import Studio
from tag.models import Tag 
from staff.models import Staff

class AllAppsView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'users': User.objects.all().values('id', 'username'),
            'animes': Anime.objects.all().values('id', 'title'),
            'mangas': Manga.objects.all().values('id', 'title'),
            'studios': Studio.objects.all().values('id', 'name'),
            'tag': Tag.objects.all().values('id', 'name'),
            'staff': Staff.objects.all().values('id', 'name'),
        }
        return Response(data)