from django.db.models import Count, Q
from django.shortcuts import render
from django.views import View

from songs.models import Song


class GetAllSongsView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        if album_id:
            songs = Song.objects.filter(album_id=album_id)
        else:
            songs = Song.objects.all()
        songs = songs.annotate(num_of_times_played=Count('playedsong'))
        self.context = {
            'songs': songs
        }
        return render(request, 'reports/songs.html', self.context)


class GetAllSongsInYearView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        year = self.kwargs['year']
        if album_id:
            songs = Song.objects.filter(album_id=album_id)
        else:
            songs = Song.objects.all()
        songs = songs.annotate(num_of_times_played=Count('playedsong', filter=Q(created_at__year=year)))
        self.context = {
            'songs': songs
        }
        return render(request, 'reports/songs.html', self.context)


class GetAllSongsInMonthView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        year = self.kwargs['year']
        month = self.kwargs['month']
        if album_id:
            songs = Song.objects.filter(album_id=album_id)
        else:
            songs = Song.objects.all()
        songs = songs.annotate(
            num_of_times_played=Count('playedsong', filter=Q(created_at__year=year, created_at__month=month))
        )
        self.context = {
            'songs': songs
        }
        return render(request, 'reports/songs.html', self.context)


class GetAllSongsOnDayView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        year = self.kwargs['year']
        month = self.kwargs['month']
        if album_id:
            songs = Song.objects.filter(album_id=album_id)
        else:
            songs = Song.objects.all()
        songs = songs.annotate(
            num_of_times_played=Count(
                'playedsong', filter=Q(created_at__year=year, created_at__month=month, created_at__day=day)
            )
        )
        self.context = {
            'songs': songs
        }
        return render(request, 'reports/songs.html', self.context)
