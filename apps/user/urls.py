from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("user", UserViewSet, basename="user")
router.register("alluser", AllUserViewSet, basename="alluser")
router.register("resetpassword", ResetPasswordViewSet, basename="resetpassword")
router.register("forgotpassword", ForgotPasswordViewSet, basename="forgotpassword")

urlpatterns = [
    path('', include(router.urls))
]
