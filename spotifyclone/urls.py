from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('signup/', users.views.signup, name="signup"),
    path('login/', users.views.user_login, name="login"),
    path('playlists/', include('playlists.urls')),
    path('songs/', include('songs.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
