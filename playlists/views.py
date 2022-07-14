from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from playlists.models import Playlist
from playlists.serializers import PlaylistSerializer
from songs.models import Song


class PlaylistView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]


class AddSongToPlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, song_id, playlist_id):
        playlist = get_object_or_404(Playlist, id=playlist_id)
        song = get_object_or_404(Song, id=song_id)
        playlist.songs.add(song)
        return JsonResponse(status=status.HTTP_201_CREATED, data="Song added to the Playlist successfully", safe=False)


class RemoveSongFromPlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, song_id, playlist_id):
        playlist = get_object_or_404(Playlist, id=playlist_id)
        song = get_object_or_404(Song, id=song_id)
        playlist.songs.remove(song)
        return JsonResponse(status=status.HTTP_200_OK, data="Song removed from the Playlist successfully", safe=False)
