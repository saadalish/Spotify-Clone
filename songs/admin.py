from django.contrib import admin

from .models import Song, SongArtist, Album, AlbumArtist

admin.site.register(Album)
admin.site.register(AlbumArtist)
admin.site.register(Song)
admin.site.register(SongArtist)


