from django.urls import include, path
from rest_framework.routers import DefaultRouter  
from user.views import UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('User', UserView, basename='user')

urlpatterns = [
    path('create/', UserView.as_view({
        'post': 'create'
    })),
    path("", include(router.urls)),
    path('createtoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("refreshtoken/", TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', UserView.as_view({
        'post': 'login'
    })),
]   