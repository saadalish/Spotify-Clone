from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .forms import PlaylistForm
from .models import Playlist
from songs.models import Song


class GetAllPlaylistsView(View):

    def get(self, request):
        playlists = Playlist.objects.filter(user=request.user)
        context = {"playlists": playlists}
        return render(request, "playlists/index.html", context)


class CreateView(View):

    def get(self, request):
        form = PlaylistForm()
        context = {'form': form}
        return render(request, "playlists/create.html", context)

    def post(self, request):
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('home'))


class UpdateView(View):

    def get(self, request, *args, **kwargs):
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
        return render(request, "playlists/update.html", context)

    def post(self, request, *args, **kwargs):
        playlist_id = self.kwargs.get('playlist_id')
        playlist = get_object_or_404(Playlist, id=playlist_id)
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))


class DeleteView(View):

    def post(self, request, *args, **kwargs):
        playlist_id = self.kwargs.get('playlist_id')
        playlist = get_object_or_404(Playlist, id=playlist_id)
        playlist.delete()
        return HttpResponseRedirect(reverse('index'))


class AddSongToPlaylistView(View):

    def post(self, request, *args, **kwargs):
        playlist_id = self.kwargs.get('playlist_id')
        song_id = self.kwargs.get('song_id')
        playlist = Playlist.objects.get(id=playlist_id)
        song = Song.objects.get(id=song_id)
        playlist.songs.add(song)
        return HttpResponseRedirect(reverse('update', args=[playlist_id]))


class RemoveSongToPlaylistView(View):

    def post(self, request, *args, **kwargs):
        playlist_id = self.kwargs.get('playlist_id')
        song_id = self.kwargs.get('song_id')
        playlist = Playlist.objects.get(id=playlist_id)
        song = Song.objects.get(id=song_id)
        playlist.songs.remove(song)
        return HttpResponseRedirect(reverse('update', args=[playlist_id]))


