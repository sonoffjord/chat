from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room, Message
from .serializers import RoomsSerializer, RoomSerializer, MessageSerializer


@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request,  slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[:10]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


class MessageView(ListCreateAPIView):
    queryset = Message.objects.all().select_related('room', 'user').only('user__username', 'room__name', 'content', 'date_added')
    serializer_class = MessageSerializer

class RoomView(ModelViewSet):
    lookup_field = 'slug'

    def get_queryset(self):
        if self.action == 'list':
            return Room.objects.all().values('name')
        
        if self.action == 'retrieve':
            return Room.objects.all().only('messages__content', 'messages__user__username')


    def get_serializer_class(self):
        if self.action == 'list':
            return RoomsSerializer

        if  self.action == 'put':
            return MessageSerializer

        return RoomSerializer
