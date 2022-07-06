from django.urls import path

from songs.views import (
    GetAllSongsView,
    AddSongView,
    UpdateSongView,
    DeleteSongView,
    GetAllAlbumsView,
    AddAlbumView,
    UpdateAlbumView,
    AlbumView,
    DeleteAlbumView,
    AddSongToAlbumView

)
from . import views

urlpatterns = [

    path('', GetAllSongsView.as_view(), name='get_all_songs'),
    path('add', AddSongView.as_view(), name='add_song'),
    path('<song_id>/update', UpdateSongView.as_view(), name='update_song'),
    path('<song_id>/delete', DeleteSongView.as_view(), name='delete_song'),
    path('albums', GetAllAlbumsView.as_view(), name='albums'),
    path('album/add', AddAlbumView.as_view(), name='add_album'),
    path('album/<album_id>/update', UpdateAlbumView.as_view(), name='update_album'),
    path('album/<album_id>', AlbumView.as_view(), name='view_album'),
    path('album/<album_id>/delete', DeleteAlbumView.as_view(), name='delete_album'),
    path('<album_id>/add', AddSongToAlbumView.as_view(), name='add_song_to_album'),
    path('<album_id>/<song_id>/delete', DeleteSongView.as_view(), name='delete_song'),


]

