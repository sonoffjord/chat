from django.contrib import admin

from .models import Massage, Room


class MassageAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')
    fields = ('text', 'date')
    readonly_fields =('date',)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'username')
    fields = ('room_name',)


admin.site.register(Massage, MassageAdmin)
admin.site.register(Room, RoomAdmin)
