from rest_framework import serializers

from .models import Results

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results 
        read_only_fields = (
            'created_at',
            "updated_at"
        ),
        fields = (
            "id",
            "user_id",
            "disease",
            "confidence",
            "url"
        )