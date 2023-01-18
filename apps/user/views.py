from django.shortcuts import render

from rest_framework import viewsets, permissions

from .serializers import *
from .models import User
import hashlib
from datetime import datetime
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.core.mail import send_mail


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

    def perform_update(self, instance):
        self.object = self.get_object()
        now = str(datetime.now())
        result = hashlib.md5(now.encode())
        instance.email_verification = result.hexdigest()
        with get_connection(  
            host=settings.EMAIL_HOST, 
            port=settings.EMAIL_PORT,  
            username=settings.EMAIL_HOST_USER, 
            password=settings.EMAIL_HOST_PASSWORD, 
            use_tls=settings.EMAIL_USE_TLS  
        ) as connection:
            subject = "Reset DogDerma Password"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [str(self.object)]
            message = ("DogDerma Reset Password Link: https://dogderm.vercel.app/"+result.hexdigest())
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
        instance.save()

class ForgotPasswordViewSet(viewsets.ModelViewSet):
    serializer_class = forgotPasswordSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        email = self.request.query_params.get('email')
        return self.queryset.filter(email=email)

    
        
class ResetPasswordViewSet(viewsets.ModelViewSet):
    serializer_class = resetPasswordSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
	
    def get_queryset(self):
        return self.queryset.filter(email_verification=self.request.user.email_verification)