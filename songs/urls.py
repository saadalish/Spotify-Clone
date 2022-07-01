from django.urls import path

from . import views

urlpatterns = [
    path('albums', views.get_all_albums_of_user, name='albums'),
    path('album/create', views.create_album, name='create_album'),
    # path('/album/<album_id>', views.update_album, name='update_album'),
    # path('/album/<album_id>/delete', views.delete_album, name='delete_album')
]
