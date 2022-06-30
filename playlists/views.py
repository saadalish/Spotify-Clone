from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

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
    songs_in_playlist = SongPlaylist.objects.filter(playlist=playlist).values_list('song_id', flat=True)
    recommended_songs = Song.objects.exclude(id__in=songs_in_playlist)[:10]
    playlist_songs = Song.objects.filter(id__in=songs_in_playlist)
    if request.method == "POST":
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PlaylistForm(None, instance=playlist)
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
    return HttpResponseRedirect(reverse('index'))


def add_song(request, playlist_id, song_id):
    playlist = Playlist.objects.get(id=playlist_id)
    song = Song.objects.get(id=song_id)
    SongPlaylist.objects.create(playlist=playlist, song=song)
    # return HttpResponseRedirect(f"/playlists/{playlist.id}")
    # return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('update', args=[playlist_id]))


def remove_song_from_playlist(request, playlist_id, song_id):
    playlist = Playlist.objects.get(id=playlist_id)
    song = Song.objects.get(id=song_id)
    SongPlaylist.objects.filter(playlist=playlist, song=song).delete()
    return HttpResponseRedirect(reverse('update', args=[playlist_id]))



