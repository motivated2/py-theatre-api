from django.contrib.auth import get_user_model
from django.db import models

from py_theatre_api import settings


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)


class Genre(models.Model):
    name = models.CharField(max_length=63)


class Play(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="plays")
    genres = models.ManyToManyField(Genre, related_name="plays")


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class TheatreHall(models.Model):
    name = models.CharField(max_length=63)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row


class Performance(models.Model):
    play = models.ForeignKey(Play, related_name="performances")
    theatre_hall = models.ForeignKey(
        TheatreHall,
        related_name="performances",
        on_delete=models.CASCADE
    )
    show_time = models.DateTimeField()


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey(
        Performance,
        related_name="tickets",
        on_delete=models.CASCADE
    )
    reservation = models.ForeignKey(
        Reservation,
        related_name="tickets",
        on_delete=models.CASCADE
    )
