from django.urls import path

from . import views

urlpatterns = [
    path('songs/', views.get_all_songs, name='get_all_songs'),
    path('songs/<album_id>', views.get_all_songs, name='get_all_album_songs'),
    path('songs/year/<int:year>', views.get_all_songs_in_year, name='get_all_songs_in_year'),
    path('songs/<album_id>/year/<int:year>', views.get_all_songs_in_year, name='get_all_album_songs_in_year'),
    path('songs/year/<int:year>/month/<int:month>', views.get_all_songs_in_month, name='get_all_songs_in_month'),
    path(
        'songs/<album_id>/year/<int:year>/month/<int:month>',
        views.get_all_songs_in_month,
        name='get_all_album_songs_in_month'
    ),
    path(
        'songs/year/<int:year>/month/<int:month>/day/<int:day>',
        views.get_all_songs_on_day,
        name='get_all_songs_on_day'
    ),
    path(
        'songs/<album_id>/year/<int:year>/month/<int:month>/day/<int:day>',
        views.get_all_songs_on_day,
        name='get_all_album_songs_on_day'
    ),

]
