from django.shortcuts import render
from django.views import View

from songs.models import Album, Song
from playlists.models import Playlist


class HomeView(View):
    context = {}

    def get(self, request):
        albums = Album.objects.all()
        if request.user.is_authenticated:
            playlists = Playlist.objects.filter(user=request.user)
            user_albums = albums.filter(artists=request.user)
            songs = Song.objects.filter(artists=request.user, type="Single")
            self.context['playlists'] = playlists
            self.context['user_albums'] = user_albums
            self.context['songs'] = songs
        self.context['albums'] = albums
        return render(request, 'home/home.html', self.context)
