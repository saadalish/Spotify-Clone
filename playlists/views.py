from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from playlists.models import Playlist
from playlists.serializers import PlaylistSerializer
from songs.models import Song


class PlaylistViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        playlists = Playlist.objects.filter(user=self.request.user)
        serializer = PlaylistSerializer(playlists, many=True)
        return JsonResponse(status=status.HTTP_200_OK, data=serializer.data, safe=False)

    def create(self, request):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)
            return JsonResponse(status=status.HTTP_201_CREATED, data=serializer.data)

    def retrieve(self, request, pk):
        playlist = get_object_or_404(Playlist, id=pk)
        serializer = PlaylistSerializer(playlist)
        return JsonResponse(status=status.HTTP_200_OK, data=serializer.data, safe=False)

    def update(self, request, pk=None):
        playlist = get_object_or_404(Playlist, id=pk)
        serializer = PlaylistSerializer(playlist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)

    def partial_update(self, request, pk=None):
        playlist = get_object_or_404(Playlist, id=pk)
        serializer = PlaylistSerializer(playlist, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)

    def destroy(self, request, pk):
        playlist = get_object_or_404(Playlist, id=pk)
        playlist.delete()
        return JsonResponse(status=status.HTTP_200_OK, data="Playlist deleted successfully", safe=False)


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
