from rest_framework import serializers

from .models import Clinics

class ClinicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinics 
        read_only_fields = (
            'created_at',
            "updated_at"
        ),
        fields = (
            "id",
            "clinic_name",
            "clinic_address",
            "clinic_mobile",
            "clinic_landline",
            "clinic_email",
            "clinic_fb",
            "url",
            "is_deleted"
        )