from django.contrib import admin
from django.urls import path, include

import home.views
import users.views

urlpatterns = [
    path('signup/', users.views.signup, name="signup"),
    path('login/', users.views.user_login, name="login"),
    path('logout/', users.views.user_logout, name="logout"),
    path('', home.views.index, name="home"),
    path('home/playlists/', include('playlists.urls')),
    path('home/songs/', include('songs.urls')),

]