from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Massage, Room
from .serializers import MassageSerializer, RoomSerializer


class MassageView(ListCreateAPIView):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer


class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer