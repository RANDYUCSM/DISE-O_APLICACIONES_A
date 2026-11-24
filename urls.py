from django.urls import include, path
from rest_framework import routers

from catalogo.views import AlbumViewSet, TrackViewSet

router = routers.DefaultRouter()
router.register("albumes", AlbumViewSet)
router.register("tracks", TrackViewSet)
urlpatterns = [path("api/", include(router.urls))]
