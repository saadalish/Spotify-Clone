from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import AlbumForm, SongForm
from .models import Album
from songs.models import Song


class GetAllSongsView(generic.ListView):
    template_name = 'songs/songs.html'
    context_object_name = 'songs'

    def get_queryset(self):
        return Song.objects.filter(artists=self.request.user, type="Single")


class AddSongView(generic.CreateView):
    template_name = 'songs/add_song.html'
    form_class = SongForm

    def form_valid(self, form):
        form.instance.type = "Single"
        form.save()
        return HttpResponseRedirect('/')


class UpdateSongView(generic.UpdateView):
    model = Song
    template_name = 'songs/update_song.html'
    form_class = SongForm
    pk_url_kwarg = "song_id"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('home'))


class GetAllAlbumsView(generic.ListView):
    template_name = 'songs/albums.html'
    context_object_name = 'albums'


class GetAllAlbumsOfUserView(generic.ListView):
    template_name = 'songs/user_albums.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.filter(artists=self.request.user)


class DeleteSongView(generic.DeleteView):
    model = Song
    pk_url_kwarg = "song_id"
    success_url = "/"


class AddAlbumView(generic.CreateView):
    template_name = 'songs/add_album.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')


class UpdateAlbumView(generic.TemplateView):
    model = Album
    template_name = 'songs/update_album.html'
    pk_url_kwarg = "album_id"

    def get_context_data(self, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        album = get_object_or_404(Album, id=album_id)
        songs_in_album = Song.objects.filter(album_id=album_id)
        form = AlbumForm(None, instance=album)
        context = {
            "form": form,
            "album_id": album_id,
            "songs_in_album": songs_in_album
        }
        return context


class UpdateAlbumDetailsView(generic.UpdateView):
    model = Album
    form_class = AlbumForm
    success_url = 'songs/update_album.html'
    pk_url_kwarg = "album_id"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('home'))


class AlbumView(generic.DetailView):
    model = Album
    template_name = 'songs/view_album.html'
    pk_url_kwarg = "album_id"

    def get_context_data(self, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        album = get_object_or_404(Album, id=album_id)
        songs_in_album = Song.objects.filter(album_id=album_id)
        context = {
            "album": album,
            "songs_in_album": songs_in_album
        }
        return context


class DeleteAlbumView(generic.DeleteView):
    model = Album
    success_url = "/"
    pk_url_kwarg = "album_id"


class AddSongToAlbumView(generic.CreateView):
    template_name = 'songs/create_song.html'
    form_class = SongForm
    pk_url_kwarg = "album_id"

    def form_valid(self, form):
        print("dfas")
        album_id = self.kwargs.get("album_id")
        form.instance.type = "Album"
        form.instance.album_id = album_id
        print(album_id)
        form.save()
        return HttpResponseRedirect('/')

