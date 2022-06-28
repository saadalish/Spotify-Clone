from django.conf import settings
from django.db import models

from core.models import AuditModelMixin


class Queue(AuditModelMixin):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Songs Queue of {self.user}'


class SongQueue(AuditModelMixin):

    queue = models.ForeignKey('Queue', on_delete=models.CASCADE)
    song = models.ForeignKey('songs.Song', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Songs in Queues"

    def __str__(self):
        return f'Queue: {self.queue} contains: {self.song}'
