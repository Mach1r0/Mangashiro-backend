from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimeViewSet, HighestRatedAnimeView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'create', AnimeViewSet, basename='create')
router.register(r'Highest-anime', HighestRatedAnimeView, basename='Highest-anime')

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)