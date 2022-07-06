from django.urls import path

from playlists.views import (
    GetAllPlaylistsView,
    CreateView,
    UpdateView,
    DeleteView,
    AddSongToPlaylistView,
    RemoveSongToPlaylistView

)

urlpatterns = [
    path('', GetAllPlaylistsView.as_view(), name='index'),
    path('create', CreateView.as_view(), name='create'),
    path('<playlist_id>', UpdateView.as_view(), name='update'),
    path('<playlist_id>/delete', DeleteView.as_view(), name='delete'),
    path('<playlist_id>/<song_id>/add', AddSongToPlaylistView.as_view(), name='add_song_to_playlist'),
    path('<playlist_id>/<song_id>/remove', RemoveSongToPlaylistView.as_view(), name='remove_song_from_playlist')
]
