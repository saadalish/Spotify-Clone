from django.db.models import Count, Q
from django.shortcuts import render

from songs.models import Song


def get_all_songs(request, album_id=None):

    if album_id:
        songs = Song.objects.filter(album_id=album_id)
    else:
        songs = Song.objects.all()
    songs = songs.annotate(num_of_times_played=Count('playedsong'))
    return generate_report(request, songs)


def get_all_songs_in_year(request, year, album_id=None):
    if album_id:
        songs = Song.objects.filter(album_id=album_id)
    else:
        songs = Song.objects.all()
    songs = songs.annotate(num_of_times_played=Count('playedsong', filter=Q(created_at__year=year)))
    return generate_report(request, songs)


def get_all_songs_in_month(request, year, month, album_id=None):
    if album_id:
        songs = Song.objects.filter(album_id=album_id)
    else:
        songs = Song.objects.all()
    songs = songs.annotate(
        num_of_times_played=Count('playedsong', filter=Q(created_at__year=year, created_at__month=month))
    )
    return generate_report(request, songs)


def get_all_songs_on_day(request, year, month, day, album_id=None):
    if album_id:
        songs = Song.objects.filter(album_id=album_id)
    else:
        songs = Song.objects.all()
    songs = songs.annotate(
        num_of_times_played=Count(
            'playedsong', filter=Q(created_at__year=year, created_at__month=month, created_at__day=day)
        )
    )
    return generate_report(request, songs)


def generate_report(request, songs):
    context = {
        'songs': songs
    }
    return render(request, 'reports/songs.html', context)
