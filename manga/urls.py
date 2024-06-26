from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MangaView

router = DefaultRouter()
router.register(r'manga', MangaView)

urlpatterns = [
    path('', include(router.urls))
]


