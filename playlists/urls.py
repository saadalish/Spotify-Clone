from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<playlist_id>', views.update, name='update'),
    path('<playlist_id>/delete', views.delete, name='delete'),
    path('<playlist_id>/<song_id>/add', views.add_song_to_playlist, name='add_song_to_playlist'),
    path('<playlist_id>/<song_id>/remove', views.remove_song_from_playlist, name='remove_song_from_playlist')
]
