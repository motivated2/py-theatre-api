from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from theatre.models import (
    Actor,
    Genre,
    Play,
    TheatreHall,
    Performance,
)
from theatre.serializers import (
    PlayListSerializer,
    PlayDetailSerializer,
)

PLAY_URL = reverse("theatre:play-list")
PERFORMANCE_URL = reverse("theatre:performance-list")


def sample_play(**params):
    defaults = {
        "title": "Sample play",
        "description": "Sample description",
    }
    defaults.update(params)

    return Play.objects.create(**defaults)


def sample_genre(**params):
    defaults = {
        "name": "Drama",
    }
    defaults.update(params)

    return Genre.objects.create(**defaults)


def sample_actor(**params):
    defaults = {"first_name": "George", "last_name": "Clooney"}
    defaults.update(params)

    return Actor.objects.create(**defaults)


def sample_performance(**params):
    theatre_hall = TheatreHall.objects.create(name="Blue", rows=20, seats_in_row=20)

    defaults = {
        "show_time": "2022-06-02 14:00:00",
        "play": None,
        "theatre_hall": theatre_hall,
    }
    defaults.update(params)

    return Performance.objects.create(**defaults)


def detail_url(play_id):
    return reverse("theatre:play-detail", args=[play_id])


class UnauthenticatedPlayApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(PLAY_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedPlayApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="test@test.test", password="test_password"
        )
        self.client.force_authenticate(self.user)

    def test_play_list(self):
        sample_play()
        play_with_genre = sample_play()

        genre_1 = sample_genre(name="Genre1")
        genre_2 = sample_genre(name="Genre2")

        play_with_genre.genres.add(genre_1, genre_2)

        res = self.client.get(PLAY_URL)
        plays = Play.objects.all()
        serializer = PlayListSerializer(plays, many=True)

        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_filter_plays_by_genre(self):
        play_without_genre = sample_play()
        play_with_genre_1 = sample_play(title="TestTitle1")
        play_with_genre_2 = sample_play(title="TestTitle2")

        genre_1 = sample_genre(name="Genre1")
        genre_2 = sample_genre(name="Genre2")

        play_with_genre_1.genres.add(genre_1)
        play_with_genre_2.genres.add(genre_2)

        res = self.client.get(PLAY_URL, {"genres": f"{genre_1.id},{genre_2.id}"})

        serializer_without_genre = PlayListSerializer(play_without_genre)
        serializer_with_genre_1 = PlayListSerializer(play_with_genre_1)
        serializer_with_genre_2 = PlayListSerializer(play_with_genre_2)

        self.assertIn(serializer_with_genre_1.data, res.data)
        self.assertIn(serializer_with_genre_2.data, res.data)
        self.assertNotIn(serializer_without_genre.data, res.data)

    def test_filter_plays_by_actor(self):
        play_without_actor = sample_play()
        play_with_actor_1 = sample_play(title="TestTitle1")
        play_with_actor_2 = sample_play(title="TestTitle2")

        actor_1 = sample_actor(first_name="Bob", last_name="Doe")
        actor_2 = sample_actor(first_name="Ihor", last_name="Doe")

        play_with_actor_1.actors.add(actor_1)
        play_with_actor_2.actors.add(actor_2)

        res = self.client.get(PLAY_URL, {"actors": f"{actor_1.id},{actor_2.id}"})

        serializer_without_actor = PlayListSerializer(play_without_actor)
        serializer_with_actor_1 = PlayListSerializer(play_with_actor_1)
        serializer_with_actor_2 = PlayListSerializer(play_with_actor_2)

        self.assertIn(serializer_with_actor_1.data, res.data)
        self.assertIn(serializer_with_actor_2.data, res.data)
        self.assertNotIn(serializer_without_actor.data, res.data)

    def test_retrieve_play_details(self):
        play = sample_play()
        play.genres.add(sample_genre())

        url = detail_url(play.id)

        res = self.client.get(url)

        serializer = PlayDetailSerializer(play)

        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_play_forbidden(self):
        payload = {"title": "TestTitle"}

        res = self.client.post(PLAY_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminPlayTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="admin@admin.admin", password="test_password", is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_play(self):
        payload = {
            "title": "TestTitle",
            "description": "TestDescription",
        }

        res = self.client.post(PLAY_URL, payload)
        print(res.data)
        play = Play.objects.get(id=res.data["id"])

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        for key in payload:
            self.assertEqual(payload[key], getattr(play, key))
