from django.shortcuts import render, redirect
from django.contrib.auth import login
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Massage, Room
from .serializers import MassageSerializer, RoomSerializer, RoomsSerializer
from .forms import SignUpForm


def frontpage(request):
    return render(request, 'chat/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'chat/form.html', {'form': form})


class MassageView(ListCreateAPIView):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer


class RoomView(ModelViewSet):
    queryset = Room.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            return RoomsSerializer
        return RoomSerializer