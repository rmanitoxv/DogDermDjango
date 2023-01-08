from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("user", UserViewSet, basename="user")
router.register("alluser", AllUserViewSet, basename="alluser")

urlpatterns = [
    path('', include(router.urls))
]
