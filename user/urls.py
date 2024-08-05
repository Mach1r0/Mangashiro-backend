from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    ReviewMangaViewSet,
    ReviewAnimeViewSet,
    Register, 
    UserCount,
    Login,
)

router = DefaultRouter()
router.register(r'create', UserViewSet, basename='create')
router.register(r'review-manga', ReviewMangaViewSet, basename='review-manga')
router.register(r'review-anime', ReviewAnimeViewSet, basename='review-anime')

app_name = 'user'

urlpatterns = [
    path('', include(router.urls)),
    path('count/', UserCount.as_view(), name="count"), 
    path('manga/<slug:slug>/', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
    path('register/', Register.as_view(), name='register'), 
    path('login/', Login.as_view(), name='login'),
]
