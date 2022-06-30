from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .forms import PlaylistForm
from .models import Playlist, SongPlaylist
from songs.models import Song


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
    songs_in_playlist = SongPlaylist.objects.filter(playlist__exact=playlist).values_list('song_id', flat=True)
    recommended_songs = Song.objects.exclude(id__in=songs_in_playlist)
    playlist_songs = Song.objects.filter(id__in=songs_in_playlist)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/playlists")
    context = {
        "form": form,
        "playlist": playlist,
        "recommended_songs": recommended_songs,
        "playlist_songs": playlist_songs
    }
    return render(request, "playlists/update.html", context)


def delete(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    playlist.delete()
    return HttpResponseRedirect("/playlists")


def add_song(request, playlist, song):
    playlist = Playlist.objects.get(name=playlist)
    song = Song.objects.get(title=song)
    SongPlaylist.objects.create(playlist=playlist, song=song)
    return HttpResponseRedirect(f"/playlists/{playlist.id}")


def remove_song_from_playlist(request, playlist, song):
    playlist = Playlist.objects.get(name=playlist)
    song = Song.objects.get(title=song)
    SongPlaylist.objects.filter(playlist=playlist, song=song).delete()
    return HttpResponseRedirect(f"/playlists/{playlist.id}")



