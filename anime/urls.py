from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimeViewSet, HighestRatedAnimeView, AnimeCountView
from django.conf import settings
from manga.views import MangaViewSet
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'create', AnimeViewSet, basename='create')
router.register(r'Highest-anime', HighestRatedAnimeView, basename='Highest-anime')

app_name = 'anime'

urlpatterns = [
    path('', include(router.urls)),
    path('count/', AnimeCountView.as_view(), name='count-anime'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)