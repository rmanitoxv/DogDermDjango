from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ClinicsSerializer
from .models import Clinics

class ClinicsViewSet(viewsets.ModelViewSet):
    serializer_class = ClinicsSerializer
    queryset = Clinics.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.soft_delete()