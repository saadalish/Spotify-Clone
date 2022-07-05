from django.db import models


class PlayedSong(models.Model):

    song = models.ForeignKey('songs.Song', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.song}'
