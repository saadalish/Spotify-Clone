from rest_framework import serializers
from songs.models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'type', 'album', 'publishing_house', 'file', 'artists']
