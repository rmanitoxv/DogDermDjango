from django.shortcuts import render

from rest_framework import viewsets, permissions

from .serializers import *
from .models import User
import hashlib
from datetime import datetime
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from rest_framework.response import Response



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

class ForgotPasswordViewSet(viewsets.ModelViewSet):
    serializer_class = forgotPasswordSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    
    def get_queryset(self):
        email = self.request.query_params.get('email')    
        result = self.queryset.filter(email=email)
        with get_connection(  
        host=settings.EMAIL_HOST, 
        port=settings.EMAIL_PORT,  
        username=settings.EMAIL_HOST_USER, 
        password=settings.EMAIL_HOST_PASSWORD, 
        use_tls=settings.EMAIL_USE_TLS  
        ) as connection:
            subject = "Reset DogDerma Password"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = ("DogDerma Reset Password Link: https://dogderm.vercel.app/resetpassword/"+result.values('email_verification')[0]['email_verification'])
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
        return result
        
class ResetPasswordViewSet(viewsets.ModelViewSet):
    serializer_class = resetPasswordSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        email_verification = self.request.query_params.get('email_verification')
        return self.queryset.filter(email_verification=email_verification)