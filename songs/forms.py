from django import forms

from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name", "artists"]
        labels = {'name': "Album Name"}
