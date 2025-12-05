from django.apps import AppConfig

class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_app.todo'   # full python path to this app
    label = 'todo'           # short label used by Django
