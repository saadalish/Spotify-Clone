from django.urls import path

from songs.views import (
    SongList,
    SongDetail,
    AlbumList,
    AlbumDetail

)

urlpatterns = [

    path('', SongList.as_view(), name='get_all_songs'),
    path('add', SongList.as_view(), name='add_song'),
    path('<int:pk>', SongDetail.as_view(), name='view_song'),
    path('<int:pk>/update', SongDetail.as_view(), name='update_song'),
    path('<int:pk>/delete', SongDetail.as_view(), name='delete_song'),
    path('albums', AlbumList.as_view(), name='albums'),
    path('album/add', AlbumList.as_view(), name='add_album'),
    path('album/<int:pk>/update', AlbumDetail.as_view(), name='update_album'),
    path('album/<int:pk>', AlbumDetail.as_view(), name='view_album'),
    path('album/<int:pk>/delete', AlbumDetail.as_view(), name='delete_album'),

]

