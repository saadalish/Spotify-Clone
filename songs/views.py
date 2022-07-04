from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .forms import AlbumForm, SongForm
from .models import Album
from songs.models import Song


def get_all_songs(request):
    songs = Song.objects.filter(artists=request.user, type="Single")
    context = {
        'songs': songs
    }
    return render(request, 'songs/songs.html', context)


def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.type = "Single"
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SongForm()
    context = {'form': form}
    return render(request, "songs/add_song.html", context)


def update_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == "POST":
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_all_songs'))
    else:
        form = SongForm(None, instance=song)
    context = {
        "form": form,
        "song_id": song_id,
    }
    return render(request, "songs/update_song.html", context)


def get_all_albums(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }
    return render(request, 'songs/albums.html', context)


def get_all_albums_of_user(request):
    albums = Album.objects.filter(artists=request.user)
    context = {
        'albums': albums
    }
    return render(request, 'songs/user_albums.html', context)


def delete_song(request, song_id, album_id=None):
    song = Song.objects.get(id=song_id)
    song.delete()
    if album_id:
        return HttpResponseRedirect(reverse('update_album', args=[album_id]))
    return HttpResponseRedirect("/")


def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('albums'))
    else:
        form = AlbumForm()
    context = {'form': form}
    return render(request, "songs/add_album.html", context)


def update_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs_in_album = Song.objects.filter(album_id=album_id)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('albums'))
    else:
        form = AlbumForm(None, instance=album)
    context = {
        "form": form,
        "album_id": album_id,
        "songs_in_album": songs_in_album
    }
    return render(request, "songs/update_album.html", context)


def view_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs_in_album = Song.objects.filter(album_id=album_id)
    context = {
        "album": album,
        "songs_in_album": songs_in_album
    }
    return render(request, "songs/view_album.html", context)


def delete_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    album.delete()
    return HttpResponseRedirect(reverse('albums'))


def add_song_to_album(request, album_id):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.type = "Album"
            form.instance.album_id = album_id
            form.save()
            return HttpResponseRedirect(reverse('update_album', args=[album_id]))
    else:
        form = SongForm()
    context = {'form': form}
    return render(request, "songs/create_song.html", context)


