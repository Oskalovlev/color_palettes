from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewset, PaletteViewset, ColorViewset

app_name = 'api'

router = DefaultRouter()

router.register("user", UserViewset, basename="user")
router.register("palette", PaletteViewset, basename="palette")
router.register("color", ColorViewset, basename="color")

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
