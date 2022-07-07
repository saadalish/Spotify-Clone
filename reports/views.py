from django.db.models import Count, Q
from django.shortcuts import render
from django.views import View

from songs.models import Song


class GetAllSongsView(View):

    def get(self, request, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        if album_id:
            songs = Song.objects.filter(album_id=album_id)
        else:
            songs = Song.objects.all()
        songs = songs.annotate(num_of_times_played=Count('playedsong'))
        context = {
            'songs': songs
        }
        return render(request, 'reports/songs.html', context)


class GetAllSongsInYearView(View):

    def get(self, request, *args, **kwargs):
        album_id = self.kwargs.get('album_id')
        year = self.kwargs['year']
        if album_id:
            songs = Song.objects.filter(album_id=album_id)
        else:
            songs = Song.objects.all()
        songs = songs.annotate(num_of_times_played=Count('playedsong', filter=Q(created_at__year=year)))
        context = {
            'songs': songs
        }
        return render(request, 'reports/songs.html', context)


class GetAllSongsInMonthView(View):

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
        context = {
            'songs': songs
        }
        return render(request, 'reports/songs.html', context)


class GetAllSongsOnDayView(View):

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
        context = {
            'songs': songs
        }
        return render(request, 'reports/songs.html', context)
