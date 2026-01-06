from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', views.ping),
    path('todo/', include('core_app.todo.urls')),
    path('song/', include('core_app.song.urls')),
    path('artist/', include('core_app.artist.urls')),
]
