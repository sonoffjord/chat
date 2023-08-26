from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Massage
from .serializers import MassageSerializer


class MassageView(ListCreateAPIView):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer