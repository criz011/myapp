from django.urls import path

from core_app.artist.apps import ArtistConfig
from core_app.artist.controller import ArtistController

app_name = ArtistConfig.name

urlpatterns = [
    path('create/', ArtistController.create, name='artist_create'),
    path('get_all/', ArtistController.get_all, name='artist_get_all'),
    path('get/', ArtistController.get_one, name='artist_get'),
    path('update/', ArtistController.update, name='artist_update'),
    path('delete/', ArtistController.delete, name='artist_delete'),
]
