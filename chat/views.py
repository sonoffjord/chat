from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Massage, Room
from .serializers import MassageSerializer, RoomSerializer


class MassageView(ListCreateAPIView):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer


class RoomView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer