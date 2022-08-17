from rest_framework import status

from core.tests import AccountTests
from .models import Song
from users.models import User


class SongTests(AccountTests):

    def setUp(self):
        super(SongTests, self).setUp()
        Song.objects.create(
            title='title',
            type='Album'
        )

    def test_get_all_songs(self):
        response = self.client.get(
            path='/songs/',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_song(self):
        artist = User.objects.get(username="testing_user")
        response = self.client.post(
            path='/songs/',
            data={
                "title": 'title_testing',
                "type": 'Single',
                "artists": [
                    artist.id
                ]

            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Song.objects.count(), 2)
        self.assertEqual(Song.objects.last().title, 'title_testing')

    def test_update_song(self):
        song = Song.objects.get(title="title")
        response = self.client.patch(
            path=f'/songs/{song.id}',
            data={"title": 'title_updated'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(Song.objects.last().title, 'title_updated')

    def test_delete_song(self):
        song = Song.objects.get(title="title")
        response = self.client.delete(
            path=f'/songs/{song.id}',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Song.objects.count(), 0)
