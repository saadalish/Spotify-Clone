from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_singles_of_user, name='get_all_singles_of_user'),
    path('add', views.add_song, name='add_song'),
    path('<song_id>/update', views.update_song, name='update_song'),
    path('<song_id>/delete', views.delete_song, name='delete_song'),

]
