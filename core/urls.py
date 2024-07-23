from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from user.views import UserViewSet, HighestRatedMangaView, HighestRatedAnimeView
from anime.views import AnimeViewSet
from manga.views import MangaViewSet
from studio.views import StudioViewSet
from tag.views import TagViewSet
from character.views import CharacterView
from staff.views import StaffViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'anime', AnimeViewSet, basename='anime')
router.register(r'manga', MangaViewSet, basename='manga')
router.register(r'studio', StudioViewSet, basename='studio')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'staff', StaffViewSet, basename='staff')  # Corrected basename to 'staff'
router.register(r'character', CharacterView, basename='character')
router.register(r'highest-rated-manga', HighestRatedMangaView, basename='highest-rated-manga')
router.register(r'highest-rated-anime', HighestRatedAnimeView, basename='highest-rated-anime')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  
]
