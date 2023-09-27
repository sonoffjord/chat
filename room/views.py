from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch

from .models import Room, Message
from .serializers import RoomsSerializer, RoomSerializer, MessageSerializer


@login_required
def rooms(request):
    rooms = Room.objects.all().values('name', 'slug')
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request,  slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[:10].select_related('user').only('user__username', 'user__id', 'id', 'content')

    return render(request, 'room/room.html', {'room': room, 'messages': messages})