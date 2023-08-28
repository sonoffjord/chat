from django.contrib import admin

from .models import Massage, Room


class MassageAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')
    fields = ('text', 'date', 'room', 'user')
    readonly_fields =('date',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name',)
    fields = ('room_name', 'members')


admin.site.register(Massage, MassageAdmin)
admin.site.register(Room, RoomAdmin)
