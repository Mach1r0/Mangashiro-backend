from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user.views import (
    UserViewSet,
    ReviewMangaViewSet,
    ReviewAnimeViewSet,
    HighestRatedMangaView,
    HighestRatedAnimeView,
)

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('review-manga', ReviewMangaViewSet, basename='review-manga')
router.register('review-anime', ReviewAnimeViewSet, basename='review-anime')

urlpatterns = [
    path('', include(router.urls)),
    path('highest-rated-manga/', HighestRatedMangaView.as_view(), name='highest-rated-manga'),
    path('highest-rated-anime/', HighestRatedAnimeView.as_view(), name='highest-rated-anime'),
]
