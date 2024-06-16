from django.urls import path, include
from .views import TagViewSet
from rest_framework.urls import DefaultRouter

router = DefaultRouter()
router.register('', TagViewSet)

urlpatterns = [
    path('', include(router.url))
]
