from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from .models import User

class UserSerializer(serializers.ModelSerializer):
    cpassword = serializers.CharField(required=False)
    message = serializers.CharField(required=False)
    class Meta:
        model = User 
        read_only_fields = (
            'date_joined',
            'date_updated'
        ),
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "url",
            "date_inactive",
            "password",
            "cpassword",
            "message"      
        )
        
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user 

    def update(self, instance, validated_data):
        if (instance.password != validated_data.get('cpassword')):
            if not instance.check_password(validated_data.get('cpassword')):
                instance.message = "Error"
                return instance
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.url = validated_data.get('url', instance.url)
        if instance.password == validated_data.get('password', instance.password):
            instance.password = instance.password
        else:
            instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
    
class forgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = (
            "id",
            "email",
            "email_verification"
        )

class resetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = (
            "id",
            "password",
            "email_verification"
        )

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance