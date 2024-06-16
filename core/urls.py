from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllAppsView  
from user.views import UserViewSet
from anime.views import AnimeViewSet
from manga.views import MangaViewSet
from studio.views import StudioViewSet
from tag.views import TagViewSet
from staff.views import StaffViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'anime', AnimeViewSet, basename='anime')
router.register(r'manga', MangaViewSet, basename='manga')
router.register(r'studio', StudioViewSet, basename='studio')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'staff', StaffViewSet, basename='Staff')

urlpatterns = [
    path('', AllAppsView.as_view(), name='all-apps'), 
    path('api/', include(router.urls)),  
]