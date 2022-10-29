from django.contrib import admin


# Register your models here.
from .models import Customer, Event, Room



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', ('date', 'time'), 'kind', 'attendees', 'room', 'description')
    list_display = ('name', 'date', 'room')
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Room)
class EventAdmin(admin.ModelAdmin):
    fields = ('alias', 'capacity')
    list_display = ('alias', 'capacity')
    ordering = ('capacity',)
    search_fields = ('capacity',)


