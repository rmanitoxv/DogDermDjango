from django.shortcuts import render

from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return self().get_queryset.filter(date_inactive=None)