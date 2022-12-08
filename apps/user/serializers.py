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
            "date_inactive"

        )