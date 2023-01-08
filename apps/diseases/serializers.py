from rest_framework import serializers

from .models import Diseases

class DiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diseases 
        read_only_fields = (
            'created_at',
            "updated_at"
        ),
        fields = (
            "id",
            "disease",
            "overview",
            "causes",
            "symptoms",
            "treatment",
            "treatments",
            "prevention",
            "preventions",
            "url",
            "is_deleted"
        )