from django.apps import AppConfig


class SongConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_app.song'   # full python path to this app
    label = 'song'           # short label used by Django
