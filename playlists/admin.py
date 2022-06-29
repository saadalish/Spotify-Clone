from django.contrib import admin

from .models import Playlist, SongPlaylist

admin.site.register(Playlist)
admin.site.register(SongPlaylist)
