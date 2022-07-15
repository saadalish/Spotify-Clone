from rest_framework.routers import DefaultRouter

from playlists.views import (
    PlaylistViewSet,

)

router = DefaultRouter()
router.register(r'', PlaylistViewSet, basename="Playlist")
urlpatterns = router.urls
