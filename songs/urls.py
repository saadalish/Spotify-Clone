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
    AddSongToAlbumView,
    UpdateAlbumDetailsView

)

urlpatterns = [

    path('', GetAllSongsView.as_view(), name='get_all_songs'),
    path('add', AddSongView.as_view(), name='add_song'),
    path('<slug:pk>/update', UpdateSongView.as_view(), name='update_song'),
    path('<slug:pk>/delete', DeleteSongView.as_view(), name='delete_song'),
    path('albums', GetAllAlbumsView.as_view(), name='albums'),
    path('album/add', AddAlbumView.as_view(), name='add_album'),
    path('album/<slug:pk>/update', UpdateAlbumView.as_view(), name='update_album'),
    path('album/<slug:pk>/update/details', UpdateAlbumDetailsView.as_view(), name='update_album_details'),
    path('album/<slug:pk>', AlbumView.as_view(), name='view_album'),
    path('album/<slug:pk>/delete', DeleteAlbumView.as_view(), name='delete_album'),
    path('<slug:pk>/add', AddSongToAlbumView.as_view(), name='add_song_to_album'),

]

