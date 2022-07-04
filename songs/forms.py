from django import forms


from songs.models import Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'file', 'publishing_house', 'artists']

    def __init__(self, *args, **kwargs):
        is_album = kwargs.pop('is_album')
        super(SongForm, self).__init__(*args, **kwargs)
        if is_album:
            self.fields.pop('artists')
