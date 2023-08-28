from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_name = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'комнату'
        verbose_name_plural = 'комнаты'
        ordering = ['room_name']


    def __str__(self):
        return self.room_name


class Massage(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['date']


    def __str__(self):
        return str(self.date)


