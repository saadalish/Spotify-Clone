from rest_framework import status

from .models import Playlist
from songs.models import Song
from songs.tests import SongTests
from users.models import User


class PlaylistTests(SongTests):

    def setUp(self):
        super(PlaylistTests, self).setUp()
        user = User.objects.get(username="testing_user")
        Playlist.objects.create(name="playlist", user=user)

    def test_get_all_playlists(self):
        response = self.client.get(
            path='/playlists/',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_playlist(self):
        response = self.client.post(
            path='/playlists/',
            data={'name': 'testing'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Playlist.objects.count(), 2)
        self.assertEqual(Playlist.objects.last().name, 'testing')

    def test_update_playlist(self):
        playlist = Playlist.objects.get(name="playlist")
        response = self.client.patch(
            path=f'/playlists/{playlist.id}/',
            data={'name': 'updated'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Playlist.objects.count(), 1)
        self.assertEqual(Playlist.objects.get().name, 'updated')

    def test_delete_playlist(self):
        playlist = Playlist.objects.get(name="playlist")
        response = self.client.delete(
            path=f'/playlists/{playlist.id}/',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Playlist.objects.count(), 0)

    def test_song_add_to_playlist(self):
        song = Song.objects.get(title='title')
        playlist = Playlist.objects.get(name='playlist')
        response = self.client.post(
            path=f'/playlists/{playlist.id}/add_song/{song.id}/',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_song_remove_from_playlist(self):
        song = Song.objects.get(title='title')
        playlist = Playlist.objects.get(name='playlist')
        response = self.client.post(
            path=f'/playlists/{playlist.id}/remove_song/{song.id}/',
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
