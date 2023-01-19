from django.shortcuts import render

from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets


from .serializers import DiseasesSerializer
from .models import Diseases

class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class DiseasesViewSet(viewsets.ModelViewSet):
    serializer_class = DiseasesSerializer
    queryset = Diseases.objects.all()
    permission_classes = [IsAuthenticated|ReadOnly]
    
    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.soft_delete()
