from django.contrib.auth.models import User
from django.db import models

from songs.models import CreateAndUpdateField, Song


class Playlist(CreateAndUpdateField):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Playlists"

    def __str__(self):
        return f'Playlist: {self.name} User: {self.user}'


class SongPlaylist(CreateAndUpdateField):

    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)
    song = models.ForeignKey('songs.Song', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Songs playlist"

    def __str__(self):
        return f'Playlist: {self.playlist.name} contains: {self.song}'

