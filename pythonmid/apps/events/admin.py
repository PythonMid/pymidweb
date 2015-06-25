from django.contrib import admin
from pythonmid.apps.events.models import Event, Participant, Participation, Place, Attendee


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'place', 'from_datetime', 'to_datetime', 'num_attendees', 'is_published')
    filter_horizontal = ('sponsors', 'organizers',)


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'timestamp', 'receive_news')


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    pass

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass