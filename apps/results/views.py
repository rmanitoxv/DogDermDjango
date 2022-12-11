from django.shortcuts import render

from rest_framework import viewsets, permissions

from .serializers import ResultsSerializer
from .models import Results

class ResultsViewSet(viewsets.ModelViewSet):
    serializer_class = ResultsSerializer
    queryset = Results.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save(user_id = self.request.user.id)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.soft_delete()
