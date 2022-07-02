from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_singles_of_user, name='get_all_singles_of_user'),
    path('add', views.add_song, name='add_song'),
    path('<song_id>/update', views.update_song, name='update_song'),
    path('<song_id>/delete', views.delete_song, name='delete_song'),
    path('albums', views.get_all_albums_of_user, name='albums'),
    path('album/create', views.create_album, name='create_album'),
    path('album/<album_id>', views.update_album, name='update_album'),
    path('album/<album_id>/delete', views.delete_album, name='delete_album'),
    path('<album_id>/add', views.add_song_to_album, name='add_song_to_album'),
    path('<album_id>/<song_id>/delete', views.delete_song_from_album, name='delete_song_from_album'),

]
