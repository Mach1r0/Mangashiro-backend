from django.urls import path
from user.views import UserView

urlpatterns = [
    path('create/', UserView.as_view({
        'post': 'create'
    })),
    
]
