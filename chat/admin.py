from django.contrib import admin

from .models import Massage


class MassageAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')
    fields = ('text', 'date')
    readonly_fields =('date',)

admin.site.register(Massage, MassageAdmin)
