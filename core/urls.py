from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', views.ping),
    path('todo/', include('core_app.todo.urls')),
]
