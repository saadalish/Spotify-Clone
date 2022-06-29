from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .models import Playlist
from .forms import PlaylistForm


def index(request):
    context = {"playlists": Playlist.objects.all()}
    return render(request, "playlists/index.html", context)


def create(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            render(request, "playlists/index.html")
    else:
        form = PlaylistForm()
    context = {'form': form}
    return render(request, "playlists/create.html", context)


def update(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    form = PlaylistForm(request.POST or None, instance=playlist)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/playlists")
    context = {
        "form": form,
        "playlist_id": playlist_id
    }
    return render(request, "playlists/update.html", context)


def delete(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    playlist.delete()
    return HttpResponseRedirect("/playlists")

