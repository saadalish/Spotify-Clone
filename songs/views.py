from django.shortcuts import render

from songs.models import Song


def index(request):
    all_songs = Song.objects.all()
    context = {
        'all_songs': all_songs,
    }
    return render(request, 'songs/index.html', context)
