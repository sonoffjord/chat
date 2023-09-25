from rest_framework import serializers

from .models import Room, Message


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Message
        fields = ('user', 'username', 'content', 'date_added', 'room')


# class SendMessageSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())

#     class Meta:
#         model = Message
#         fields = ('content', 'user')


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('name',)


class RoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)

    class Meta:
        model = Room
        fields = ('messages',)