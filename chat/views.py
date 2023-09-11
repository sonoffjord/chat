from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import generic
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




class MassageView(generic.ListView):
    model = Massage
    template_name = 'chat/messages.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Massage.objects.all()


class RoomView(generic.ListView):
    model = Room
    template_name = 'chat/rooms.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        return Room.objects.all()