from django.urls import path

from reports.views import (
    GetAllSongsView,
    GetAllSongsInYearView,
    GetAllSongsInMonthView,
    GetAllSongsOnDayView
)

urlpatterns = [
    path('songs/', GetAllSongsView.as_view(), name='get_all_songs'),
    path('songs/<album_id>', GetAllSongsView.as_view(), name='get_all_album_songs'),
    path('songs/year/<int:year>', GetAllSongsInYearView.as_view(), name='get_all_songs_in_year'),
    path('songs/<album_id>/year/<int:year>', GetAllSongsInYearView.as_view(), name='get_all_album_songs_in_year'),
    path('songs/year/<int:year>/month/<int:month>', GetAllSongsInMonthView.as_view(), name='get_all_songs_in_month'),
    path(
        'songs/<album_id>/year/<int:year>/month/<int:month>',
        GetAllSongsInMonthView.as_view(),
        name='get_all_album_songs_in_month'
    ),
    path(
        'songs/year/<int:year>/month/<int:month>/day/<int:day>',
        GetAllSongsOnDayView.as_view(),
        name='get_all_songs_on_day'
    ),
    path(
        'songs/<album_id>/year/<int:year>/month/<int:month>/day/<int:day>',
        GetAllSongsOnDayView.as_view(),
        name='get_all_album_songs_on_day'
    ),

]
