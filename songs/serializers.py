from rest_framework import serializers

from songs.models import Album, Song
from users.models import User
from users.serializers import UserSerializer


class SongSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(is_artist=True),
        many=True,
    )

    class Meta:
        model = Song
        fields = ['id', 'title', 'type', 'album', 'publishing_house', 'artists']

    def validate(self, attrs):
        if attrs.get('artists') and len(attrs.get('artists')) == 0:
            raise serializers.ValidationError(
                {"artists": "Empty artists list"})
        return attrs


class AlbumSerializer(serializers.ModelSerializer):
    artists = UserSerializer(many=True)
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'name', 'thumbnail', 'artists', 'songs']
