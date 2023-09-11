from django.contrib import admin

from .models import Massage, Room

@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'date')
    fields = ('text', 'date', 'room', 'user')
    readonly_fields =('date',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name',)
    fields = ('room_name', 'members')