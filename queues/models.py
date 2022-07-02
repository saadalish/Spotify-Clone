from django.conf import settings
from django.db import models

from core.models import AuditModelMixin


class Queue(AuditModelMixin):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    songs = models.ManyToManyField('songs.Song', blank=True)

    def __str__(self):
        return f'User: {self.user} Songs: {self.songs}'
