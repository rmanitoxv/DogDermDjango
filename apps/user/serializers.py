from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
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
            "email_verified_at",
            "url",
            "date_inactive",
            "password"
        )
        
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user 

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        print(instance.is_staff)
        print(validated_data['is_staff'])
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        if (instance.password != validated_data.get('password', instance.password)):
            instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance 