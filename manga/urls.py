from django.urls import path
from manga.views import MangaView

urlpatterns = [
    path('create/', MangaView.as_view({
        'post': 'create'
    })),
    
]
