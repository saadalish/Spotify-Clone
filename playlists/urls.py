from django.urls import path

from playlists.views import (
    PlaylistView,
    AddSongToPlaylistView,
    RemoveSongFromPlaylistView,

)

urlpatterns = [
    path('', PlaylistView.as_view(), name='get_all_playlists'),
    path('create', PlaylistView.as_view(), name='create_playlist'),
    path('<int:pk>', PlaylistView.as_view(), name='view_playlist'),
    path('<int:pk>/update', PlaylistView.as_view(), name='update_playlist'),
    path('<int:pk>/delete', PlaylistView.as_view(), name='delete_playlist'),
    path('<playlist_id>/<song_id>/add', AddSongToPlaylistView.as_view(), name='add_song_to_playlist'),
    path('<playlist_id>/<song_id>/remove', RemoveSongFromPlaylistView.as_view(), name='remove_song_from_playlist')
]
