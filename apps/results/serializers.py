from rest_framework import serializers

from .models import Results

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results 
        read_only_fields = (
            "updated_at"
        ),
        fields = (
            'created_at',
            "id",
            "user_id",
            "disease",
            "confidence",
            "url"
        )