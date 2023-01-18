from django.shortcuts import render

from rest_framework import viewsets, permissions

from .serializers import *
from .models import User
import hashlib
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
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save()

class forgotPasswordViewSet(viewsets.ModelViewSet):
    serializer_class = forgotPasswordSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)

    def perform_update(self, serializer):
        now = datetime.now()
        result = hashlib.md5(serializer.email + now)
        serializer.email_verification = result.hexdigest()
        serializer.save()
        
class resetPasswordViewSet(viewsets.ModelViewSet):
    serializer_class = resetPasswordSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny)
	
    def get_queryset(self):
        return self.queryset.filter(email_verification=self.request.user.email_verification)