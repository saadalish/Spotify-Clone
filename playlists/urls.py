from django.urls import path
from rest_framework.routers import DefaultRouter

from playlists.views import (
    PlaylistViewSet,
    AddSongToPlaylistView,
    RemoveSongFromPlaylistView,

)

router = DefaultRouter()
router.register(r'', PlaylistViewSet, basename="Playlist")
urlpatterns = [
    path('<playlist_id>/<song_id>/add', AddSongToPlaylistView.as_view(), name='add_song_to_playlist'),
    path('<playlist_id>/<song_id>/remove', RemoveSongFromPlaylistView.as_view(), name='remove_song_from_playlist')
]
urlpatterns += router.urls
