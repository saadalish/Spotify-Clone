from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .forms import SongForm
from songs.models import Song


def get_all_singles_of_user(request):
    singles = Song.objects.filter(artists=request.user, type="Single")
    context = {
        'singles': singles
    }
    return render(request, 'songs/songs.html', context)


def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, is_album=False)
        if form.is_valid():
            song = form.save(commit=False)
            song.type = "Single"
            song.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('get_all_singles_of_user'))
    else:
        form = SongForm(is_album=False)
    context = {'form': form}
    return render(request, "songs/create_song.html", context)


def update_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == "POST":
        form = SongForm(request.POST, request.FILES, is_album=False, instance=song)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_all_singles_of_user'))
    else:
        form = SongForm(None, is_album=False, instance=song)
    context = {
        "form": form,
        "song_id": song_id,
    }
    return render(request, "songs/update_song.html", context)


def delete_song(request, song_id):
    song = Song.objects.get(id=song_id)
    song.delete()
    return HttpResponseRedirect(reverse('get_all_singles_of_user'))
