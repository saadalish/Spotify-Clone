from django.contrib.auth.models import User
from django.db import models

from songs.models import CreateAndUpdateField


class Queue(CreateAndUpdateField):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Queues"

    def __str__(self):
        return f'{self.user}'


class SongQueue(CreateAndUpdateField):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey('songs.Song', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Songs Queue"

    def __str__(self):
        return f'{self.user}'
