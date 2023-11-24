from django.urls import path
from django.urls import path
from user.views import UserView
from .views import LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('create/', UserView.as_view(), name='user_create'),
    path('createtoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("refreshtoken/", TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(), name='login'),
]