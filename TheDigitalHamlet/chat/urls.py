# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.lobby, name="lobby"),
    path("chat/<str:room_name>/", views.room, name="room_name"),
]