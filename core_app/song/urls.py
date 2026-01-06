from django.urls import path

from core_app.song.apps import SongConfig
from .controller import SongController

app_name = SongConfig.name

urlpatterns = [
    path("create/", SongController.create, name="song_create"),
    path("get_all/", SongController.get_all, name="song_get_all"),
    path("get/", SongController.get_one, name="song_get"),
    path("update/", SongController.update, name="song_update"),
    path("delete/", SongController.delete, name="song_delete"),
]
