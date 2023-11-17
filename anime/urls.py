from django.urls import path
from anime.views import AnimeView

urlpatterns = [
    path('create/', AnimeView.as_view({
        'post': 'create'
    })),
    
]
