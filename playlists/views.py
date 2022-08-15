from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action


from playlists.models import Playlist
from playlists.serializers import PlaylistSerializer
from songs.models import Song


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(
        detail=True,
        url_path=r'add_song/(?P<song_id>[^/.]+)',
        methods=['post']
    )
    def add_song_to_playlist(self, request, pk, song_id):
        playlist = get_object_or_404(Playlist, id=pk)
        song = get_object_or_404(Song, id=song_id)
        playlist.songs.add(song)
        return JsonResponse(
            status=status.HTTP_200_OK,
            data="Song added from the Playlist successfully",
            safe=False
        )

    @action(
        detail=True,
        url_path=r'remove_song/(?P<song_id>[^/.]+)',
        methods=['post']
    )
    def remove_song_from_playlist(self, request, pk, song_id):
        playlist = get_object_or_404(Playlist, id=pk)
        song = get_object_or_404(Song, id=song_id)
        playlist.songs.remove(song)
        return JsonResponse(
            status=status.HTTP_204_NO_CONTENT,
            data="Song removed from the Playlist successfully",
            safe=False
        )
