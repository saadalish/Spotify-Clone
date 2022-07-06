from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .forms import AlbumForm, SongForm
from .models import Album
from songs.models import Song


class GetAllSongsView(View):

    def get(self, request):
        songs = Song.objects.filter(artists=request.user, type="Single")
        context = {
            'songs': songs
        }
        return render(request, 'songs/songs.html', context)


class AddSongView(View):

    def get(self, request):
        form = SongForm()
        context = {'form': form}
        return render(request, "songs/add_song.html", context)

    def post(self, request):
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.type = "Single"
            form.save()
            return HttpResponseRedirect('/')


class UpdateSongView(View):

    def get(self, request, *args, **kwargs):
        song_id = self.kwargs.get('song_id')
        song = get_object_or_404(Song, id=song_id)
        form = SongForm(None, instance=song)
        context = {
            'form': form,
            "song_id": song_id
        }
        return render(request, "songs/update_song.html", context)

    def post(self, request, *args, **kwargs):
        song_id = self.kwargs.get('song_id')
        song = get_object_or_404(Song, id=song_id)
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_all_songs'))


class GetAllAlbumsView(View):

    def get(self, request):
        albums = Album.objects.all()
        context = {
            'albums': albums
        }
        return render(request, 'songs/albums.html', context)


class GetAllAlbumsOfUserView(View):

    def get(self, request):
        albums = Album.objects.filter(artists=request.user)
        context = {
            'albums': albums
        }
        return render(request, 'songs/user_albums.html', context)


class DeleteSongView(View):

    def post(self, request, *args, **kwargs):
        song_id = self.kwargs.get('song_id')
        album_id = self.kwargs.get('album_id')
        song = Song.objects.get(id=song_id)
        song.delete()
        if album_id:
            return HttpResponseRedirect(reverse('update_album', args=[album_id]))
        return HttpResponseRedirect("/")


class AddAlbumView(View):

    def get(self, request):
        form = AlbumForm()
        context = {'form': form}
        return render(request, "songs/add_album.html", context)

    def post(self, request):
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('albums'))


class UpdateAlbumView(View):

    def get(self, request, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        album = get_object_or_404(Album, id=album_id)
        songs_in_album = Song.objects.filter(album_id=album_id)
        form = AlbumForm(None, instance=album)
        context = {
            "form": form,
            "album_id": album_id,
            "songs_in_album": songs_in_album
        }
        return render(request, "songs/update_album.html", context)

    def post(self, request, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        album = get_object_or_404(Album, id=album_id)
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('albums'))


class AlbumView(View):

    def get(self, request, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        album = get_object_or_404(Album, id=album_id)
        songs_in_album = Song.objects.filter(album_id=album_id)
        context = {
            "album": album,
            "songs_in_album": songs_in_album
        }
        return render(request, "songs/view_album.html", context)


class DeleteAlbumView(View):

    def post(self, request, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        album = get_object_or_404(Album, id=album_id)
        album.delete()
        return HttpResponseRedirect(reverse('albums'))


class AddSongToAlbumView(View):

    def get(self, request, *args, **kwargs):
        form = SongForm()
        context = {'form': form}
        return render(request, "songs/create_song.html", context)

    def post(self, request, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.type = "Album"
            form.instance.album_id = album_id
            form.save()
            return HttpResponseRedirect(reverse('update_album', args=[album_id]))


