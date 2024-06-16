from .views import StaffViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter
router.register(r'staff', StaffViewSet)

urlpatterns = [
    path('', include(router.urls))
]
