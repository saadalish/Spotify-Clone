from django import forms

from .models import Album
from songs.models import Song


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name", "thumbnail", "publishing_house", "artists"]


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'file', 'publishing_house', 'artists']

