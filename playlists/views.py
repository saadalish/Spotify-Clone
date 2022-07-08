from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views import generic

from .forms import PlaylistForm
from .models import Playlist
from songs.models import Song


class GetAllPlaylistsView(generic.ListView):
    template_name = 'playlists/get_all_playlists.html'
    context_object_name = 'playlists'

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)


class CreatePlaylistView(generic.CreateView):
    template_name = 'playlists/create_playlist.html'
    form_class = PlaylistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return HttpResponseRedirect(reverse('home'))


class PlaylistView(generic.TemplateView):
    model = Playlist
    template_name = 'playlists/view_playlist.html'
    pk_url_kwarg = "playlist_id"

    def get_context_data(self, *args, **kwargs):
        playlist_id = self.kwargs.get('playlist_id')
        playlist = get_object_or_404(Playlist, id=playlist_id)
        form = PlaylistForm(None, instance=playlist)
        songs_in_playlist = playlist.songs.values_list('id', flat=True)
        recommended_songs = Song.objects.exclude(id__in=songs_in_playlist)[:10]
        context = {
            "form": form,
            "playlist": playlist,
            "recommended_songs": recommended_songs,
            "playlist_songs": playlist.songs.all()
        }
        return context


class UpdatePlaylistView(generic.UpdateView):
    model = Playlist
    form_class = PlaylistForm
    pk_url_kwarg = "playlist_id"
    template_name = "playlists/update_playlist.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return HttpResponseRedirect('/')


class DeletePlaylistView(generic.DeleteView):
    model = Playlist
    success_url = "/"
    pk_url_kwarg = "playlist_id"


class AddSongToPlaylistView(View):

    def post(self, request, *args, **kwargs):
        playlist_id = self.kwargs.get('playlist_id')
        song_id = self.kwargs.get('song_id')
        playlist = Playlist.objects.get(id=playlist_id)
        song = Song.objects.get(id=song_id)
        playlist.songs.add(song)
        return HttpResponseRedirect(reverse('view_playlist', args=[playlist_id]))


class RemoveSongToPlaylistView(View):

    def post(self, request, *args, **kwargs):
        playlist_id = self.kwargs.get('playlist_id')
        song_id = self.kwargs.get('song_id')
        playlist = Playlist.objects.get(id=playlist_id)
        song = Song.objects.get(id=song_id)
        playlist.songs.remove(song)
        return HttpResponseRedirect(reverse('view_playlist', args=[playlist_id]))
