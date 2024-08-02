from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from anime.views import AnimeViewSet
from user.views import UserViewSet
from manga.views import MangaViewSet
from studio.views import StudioViewSet
from tag.views import TagViewSet
from character.views import CharacterView
from staff.views import StaffViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'anime', AnimeViewSet, basename='anime')
router.register(r'manga', MangaViewSet, basename='manga')
router.register(r'studio', StudioViewSet, basename='studio')
router.register(r'user', UserViewSet, basename='user')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'staff', StaffViewSet, basename='staff')  
router.register(r'character', CharacterView, basename='character')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  
    path('manga/', include('manga.urls', namespace='manga')),
    path('anime/', include('anime.urls', namespace='anime')),  
    path('', include(router.urls)),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)