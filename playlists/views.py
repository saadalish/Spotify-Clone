from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .forms import PlaylistForm
from .models import Playlist
from songs.models import Song


def index(request):

    playlists = Playlist.objects.filter(user=request.user)
    context = {"playlists": playlists}
    return render(request, "playlists/index.html", context)


def create(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PlaylistForm()
    context = {'form': form}
    return render(request, "playlists/create.html", context)


def update(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    songs_in_playlist = playlist.songs.values_list('id', flat=True)
    recommended_songs = Song.objects.exclude(id__in=songs_in_playlist)[:10]
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
        "playlist_songs": playlist.songs.all()
    }
    return render(request, "playlists/update.html", context)


def delete(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    playlist.delete()
    return HttpResponseRedirect(reverse('index'))


def add_song_to_playlist(request, playlist_id, song_id):
    playlist = Playlist.objects.get(id=playlist_id)
    song = Song.objects.get(id=song_id)
    playlist.songs.add(song)
    return HttpResponseRedirect(reverse('update', args=[playlist_id]))


def remove_song_from_playlist(request, playlist_id, song_id):
    playlist = Playlist.objects.get(id=playlist_id)
    song = Song.objects.get(id=song_id)
    playlist.songs.remove(song)
    return HttpResponseRedirect(reverse('update', args=[playlist_id]))



