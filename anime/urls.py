from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimeView

router = DefaultRouter()
router.register(r'anime', AnimeView, basename='anime')

urlpatterns = [
    path('', include(router.urls)),
]