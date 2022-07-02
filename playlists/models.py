from django.conf import settings
from django.db import models

from core.models import AuditModelMixin


class Playlist(AuditModelMixin):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    songs = models.ManyToManyField('songs.Song', blank=True)

    def __str__(self):
        return f'Playlist: {self.name} User: {self.user} Songs: {self.songs}'
