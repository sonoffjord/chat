from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Massage, Room


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class MassageSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Massage
        fields = ('text', 'date', 'user')


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_name',)


class RoomSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    messages = MassageSerializer(many=True)

    class Meta:
        model = Room
        fields = ('room_name', 'members', 'messages')