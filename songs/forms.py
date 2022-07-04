from django import forms


from songs.models import Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'file', 'publishing_house', 'artists']
