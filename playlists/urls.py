from django.urls import path

from playlists.views import (
    GetAllPlaylistsView,
    CreatePlaylistView,
    PlaylistView,
    DeletePlaylistView,
    AddSongToPlaylistView,
    RemoveSongToPlaylistView,
    UpdatePlaylistView

)


urlpatterns = [
    path('', GetAllPlaylistsView.as_view(), name='get_all_playlists'),
    path('create', CreatePlaylistView.as_view(), name='create_playlist'),
    path('<int:playlist_id>', PlaylistView.as_view(), name='view_playlist'),
    path('<int:playlist_id>/update', UpdatePlaylistView.as_view(), name='update_playlist'),
    path('<int:playlist_id>/delete', DeletePlaylistView.as_view(), name='delete_playlist'),
    path('<playlist_id>/<song_id>/add', AddSongToPlaylistView.as_view(), name='add_song_to_playlist'),
    path('<playlist_id>/<song_id>/remove', RemoveSongToPlaylistView.as_view(), name='remove_song_from_playlist')
]
