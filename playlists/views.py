from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from playlists.models import Playlist
from playlists.serializers import PlaylistSerializer
from songs.models import Song


class PlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    # list
    def get(self, request):
        playlists = Playlist.objects.filter(user=self.request.user)
        serializer = PlaylistSerializer(playlists, many=True)
        return JsonResponse(status=status.HTTP_200_OK, data=serializer.data, safe=False)

    # create
    def post(self, request):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)
            return JsonResponse(status=status.HTTP_201_CREATED, data=serializer.data)


class PlaylistDetail(APIView):

    # retrieve
    def get(self, request, pk):
        playlist = get_object_or_404(Playlist, id=pk)
        serializer = PlaylistSerializer(playlist)
        return JsonResponse(status=status.HTTP_200_OK, data=serializer.data, safe=False)

    # update
    def put(self, request, pk):
        playlist = get_object_or_404(Playlist, id=pk)
        serializer = PlaylistSerializer(playlist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)

    # destroy
    def delete(self, request, pk):
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
