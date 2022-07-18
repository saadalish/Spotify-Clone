from rest_framework import serializers

from songs.models import Album, Song
from users.serializers import UserSerializer


class SongSerializer(serializers.ModelSerializer):
    artists = UserSerializer(many=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'type', 'album', 'publishing_house', 'file', 'artists']


class AlbumSerializer(serializers.ModelSerializer):
    artists = UserSerializer(many=True)
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'name', 'thumbnail', 'artists', 'songs']
