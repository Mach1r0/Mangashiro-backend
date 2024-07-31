from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    ReviewMangaViewSet,
    ReviewAnimeViewSet,
    AnimeStateViewSet,
    MangaStateViewSet,
    Register, 
    Login,
)

router = DefaultRouter()
router.register(r'create', UserViewSet, basename='create')
router.register(r'review-manga', ReviewMangaViewSet, basename='review-manga')
router.register(r'review-anime', ReviewAnimeViewSet, basename='review-anime')
router.register(r'user-status-anime', AnimeStateViewSet, basename='user-status-anime')
router.register(r'user-status-manga', MangaStateViewSet, basename='user-status-manga')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', Register.as_view(), name='register'), 
    path('login/', Login.as_view(), name='login'),
]
