from django.shortcuts import render

from .forms import AlbumForm
from .models import Album


def get_all_albums_of_user(request):

    albums = Album.objects.filter(artists=request.user)
    context = {
        'albums': albums
    }
    return render(request, 'songs/albums.html', context)


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            render(request, "songs/albums.html")
    else:
        form = AlbumForm()
    context = {'form': form}
    return render(request, "songs/create_album.html", context)
