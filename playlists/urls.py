from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<playlist_id>', views.update, name='update'),
    path('<playlist_id>/delete', views.delete, name='delete'),
]
