from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from playlists.models import Playlist
from playlists.serializers import PlaylistSerializer
from songs.models import Song


class GetAllPlaylistsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        playlists = Playlist.objects.filter(user=self.request.user)
        serializer = PlaylistSerializer(playlists, many=True)
        return JsonResponse(serializer.data)


class CreatePlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.data:
            serializer = PlaylistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=self.request.user)
                return Response({
                    "status": True,
                    "message": request.data
                })
            return Response({
                "status": False,
                "message": "Invalid Input",
                "Error": serializer.errors
            })
        else:
            raise ValueError("Empty playlist object in request. Create API needs a json object")


class PlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, playlist_id):
        try:
            playlist = Playlist.objects.get(id=playlist_id)
            serializer = PlaylistSerializer(playlist)
            return JsonResponse(serializer.data)
        except ObjectDoesNotExist:
            return Response({
                "status": False,
                "message": f"No Playlist exist with id {playlist_id}"
            })


class UpdatePlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, playlist_id):
        try:
            playlist = Playlist.objects.get(id=playlist_id)
            request_data = JSONParser().parse(request)
            serializer = PlaylistSerializer(playlist, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({
                "status": False,
                "message": f"No Playlist exist with id {playlist_id}"
            })


class DeletePlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, playlist_id):
        try:
            playlist = Playlist.objects.get(id=playlist_id)
            playlist.delete()
            return Response({
                "status": True,
                "message": "Playlist deleted successfully"
            })
        except ObjectDoesNotExist:
            return Response({
                "status": False,
                "message": f"No Playlist exist with id {playlist_id}"
            })


class AddSongToPlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, song_id, playlist_id):
        try:
            playlist = Playlist.objects.get(id=playlist_id)
            song = Song.objects.get(id=song_id)
            playlist.songs.add(song)
            return Response({
                "status": True,
                "message": "Song added to the Playlist successfully"
            })
        except ObjectDoesNotExist:
            return Response({
                "status": False,
                "message": f"No Playlist/Song exist with id {playlist_id}"
            })


class RemoveSongToPlaylistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, song_id, playlist_id):
        try:
            playlist = Playlist.objects.get(id=playlist_id)
            song = Song.objects.get(id=song_id)
            playlist.songs.remove(song)
            return Response({
                "status": True,
                "message": "Song removed from the Playlist successfully"
            })
        except ObjectDoesNotExist:
            return Response({
                "status": False,
                "message": f"No Playlist/Song exist with id {playlist_id}"
            })
