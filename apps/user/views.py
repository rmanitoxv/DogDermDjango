from django.shortcuts import render

from rest_framework import viewsets

from .serializers import *
from .models import User

from datetime import datetime

class AllUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_active=1)

    def perform_destroy(self, instance):
        instance.is_active = 0
        instance.date_inactive = datetime.now()
        instance.save()
        
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)
