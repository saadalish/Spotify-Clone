from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .forms import SongForm
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
            song = form.save(commit=False)
            song.type = "Single"
            song.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('get_all_songs'))
    else:
        form = SongForm()
    context = {'form': form}
    return render(request, "songs/create_song.html", context)


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


def delete_song(request, song_id):
    song = Song.objects.get(id=song_id)
    song.delete()
    return HttpResponseRedirect(reverse('get_all_songs'))
