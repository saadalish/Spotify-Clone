from django.urls import path

from . import views

urlpatterns = [
    path('albums', views.get_all_albums, name='albums'),
    path('album/add', views.add_album, name='add_album'),
    path('album/<album_id>', views.update_album, name='update_album'),
    path('album/<album_id>/delete', views.delete_album, name='delete_album'),
    path('<album_id>/add', views.add_song_to_album, name='add_song_to_album'),
    path('<album_id>/<song_id>/delete', views.delete_song_from_album, name='delete_song_from_album'),

]