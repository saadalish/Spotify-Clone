from django.shortcuts import render

from songs.models import Album, Song
from playlists.models import Playlist


def home(request):
    context = {}
    albums = Album.objects.all()
    if request.user.is_authenticated:
        playlists = Playlist.objects.filter(user=request.user)
        user_albums = albums.filter(artists=request.user)
        songs = Song.objects.filter(artists=request.user, type="Single")
        context['playlists'] = playlists
        context['user_albums'] = user_albums
        context['songs'] = songs
    context['albums'] = albums
    return render(request, 'home/home.html', context)
