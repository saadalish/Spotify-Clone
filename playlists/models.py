from django.conf import settings
from django.db import models

from core.models import AuditModelMixin


class Playlist(AuditModelMixin):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class SongPlaylist(AuditModelMixin):

    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)
    song = models.ForeignKey('songs.Song', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Songs in playlists"

    def __str__(self):
        return f'Playlist: {self.playlist} contains: {self.song}'
