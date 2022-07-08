from django.views import generic

from songs.models import Album, Song
from playlists.models import Playlist


class HomeView(generic.TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = {}
        albums = Album.objects.all()
        if self.request.user.is_authenticated:
            playlists = Playlist.objects.filter(user=self.request.user)
            user_albums = albums.filter(artists=self.request.user)
            songs = Song.objects.filter(artists=self.request.user, type="Single")
            context['playlists'] = playlists
            context['user_albums'] = user_albums
            context['songs'] = songs
        context['albums'] = albums
        return context

