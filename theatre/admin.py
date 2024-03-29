from django.contrib import admin
from theatre.models import (
    Actor,
    Genre,
    Play,
    Reservation,
    TheatreHall,
    Performance,
    Ticket,
)


admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Play)
admin.site.register(Reservation)
admin.site.register(TheatreHall)
admin.site.register(Performance)
admin.site.register(Ticket)
