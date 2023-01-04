from django.shortcuts import render

from rest_framework import viewsets, permissions

from .serializers import ClinicsSerializer
from .models import Clinics

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
             
        return request.user


class ClinicsViewSet(viewsets.ModelViewSet):
    serializer_class = ClinicsSerializer
    queryset = Clinics.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.soft_delete()