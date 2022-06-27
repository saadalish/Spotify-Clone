from django.db import models

from users.models import Artist


class CreateAndUpdateField(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Song(CreateAndUpdateField):

    title = models.CharField(max_length=100)
    SONG_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Album', 'Album'),
    ]
    type = models.CharField(max_length=10, choices=SONG_TYPE_CHOICES)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, blank=True, null=True)
    source = models.URLField(max_length=255)
    details = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = "Songs"

    def __str__(self):
        return f'{self.title}'


class SongArtist(CreateAndUpdateField):

    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Song Artists"

    def __str__(self):
        return f'{self.song} has following artists: {self.artist}'


class Album(CreateAndUpdateField):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Albums"

    def __str__(self):
        return f'{self.name}'


class AlbumArtist(CreateAndUpdateField):

    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Album Artists"

    def __str__(self):
        return f'{self.album} has following artists: {self.artist}'

