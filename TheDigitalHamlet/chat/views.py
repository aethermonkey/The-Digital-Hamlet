# chat/views.py
from django.shortcuts import render
from django.shortcuts import get_object_or_404

def lobby(request):
    return render(request, "chat/lobby.html")

def room(request, room_name):
    print(room_name)
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })