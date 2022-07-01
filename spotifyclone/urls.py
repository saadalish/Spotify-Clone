from django.contrib import admin
from django.urls import path, include

import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', users.views.signup, name="signup"),
    path('login/', users.views.user_login, name="login"),
    path('playlists/', include('playlists.urls')),
    path('songs/', include('songs.urls')),
]
