from django.conf import settings
from django.db import models

from core.models import AuditModelMixin


class Song(AuditModelMixin):

    title = models.CharField(max_length=100)
    SONG_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Album', 'Album'),
    ]
    type = models.CharField(max_length=10, choices=SONG_TYPE_CHOICES)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='uploads/songs/')
    publishing_house = models.CharField(max_length=255, null=True)
    artists = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'is_artist': True},
        blank=True
    )

    def __str__(self):
        return f'{self.title}'


class Album(AuditModelMixin):

    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='uploads/album_thumbnails')
    publishing_house = models.CharField(max_length=255, null=True)
    artists = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'is_artist': True},
        blank=True
    )

    def __str__(self):
        return f'{self.name}'
