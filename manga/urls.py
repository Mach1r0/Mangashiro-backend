from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MangaViewSet, HighestRatedMangaView, MangaCountViews

router = DefaultRouter()
router.register(r'create', MangaViewSet, basename='create')
router.register(r'highest-rated-manga', HighestRatedMangaView, basename='highest-rated-manga')

app_name = 'manga'

urlpatterns = [
    path('', include(router.urls)),
    path('count', MangaCountViews.as_view(), name='count'), 
    path('manga/<slug:slug>/', MangaViewSet.as_view({'get': 'retrieve'}), name='manga-detail'),
]
