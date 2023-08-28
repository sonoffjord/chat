from django.contrib import admin

from .models import Massage, Room


class MassageAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')
    fields = ('text', 'date')
    readonly_fields =('date',)

    def create_time_display(self, obj):
        return obj.date.strftime("%B %d, %Y")
    
    create_time_display.short_description = '<желаемое имя>'


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name',)
    fields = ('room_name',)


admin.site.register(Massage, MassageAdmin)
admin.site.register(Room, RoomAdmin)
