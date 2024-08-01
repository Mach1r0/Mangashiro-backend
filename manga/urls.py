from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MangaViewSet, HighestRatedMangaView

router = DefaultRouter()
router.register(r'create', MangaViewSet, basename='create')
router.register(r'highest-rated-manga', HighestRatedMangaView, basename='HighestRated')

urlpatterns = [
    path('', include(router.urls)),
]
