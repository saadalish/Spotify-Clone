from django.shortcuts import render

from songs.models import Album, Song
from playlists.models import Playlist


def index(request):
    context = {}
    if request.user.is_authenticated:
        playlists = Playlist.objects.filter(user=request.user)
        user_albums = Album.objects.filter(artists=request.user)
        singles = Song.objects.filter(artists=request.user, type="Single")
        context['playlists'] = playlists
        context['user_albums'] = user_albums
        context['singles'] = singles
    albums = Album.objects.all()
    context['albums'] = albums
    return render(request, 'home/index.html', context)
