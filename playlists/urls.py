from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<playlist_id>', views.update, name='update'),
    path('<playlist_id>/delete', views.delete, name='delete'),
    path('<playlist>/<song>/add', views.add_song, name='AddSongPlaylist'),
    path('<playlist>/<song>/remove', views.remove_song_from_playlist, name='RemoveSongPlaylist')
]
