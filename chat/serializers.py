from rest_framework import serializers

from .models import Massage, Room


class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields = ('text', 'date')


class RoomSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')

    class Meta:
        model = Room
        fields = ('room_name', 'username')