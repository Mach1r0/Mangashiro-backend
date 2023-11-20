from django.urls import path
from studio.view import StudioView

urlpatterns = [
    path('create/', StudioView.as_view({
        'post': 'create'
    })),
    
]
