from django.urls import path, include
from .views import TagViewSet
from rest_framework.urls import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('', TagViewSet)

urlpatterns = [
    path('', include(router.url))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
