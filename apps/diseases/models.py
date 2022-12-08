from django.contrib.auth.models import models
from django.db import models
from datetime import datetime

# Create your models here.
class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class Diseases(SoftDeleteModel):
    disease = models.TextField(unique=True)
    overview = models.TextField(max_length=999)
    causes = models.TextField(max_length=999)
    symptoms = models.TextField(max_length=999)
    treatment = models.TextField(max_length=999)
    prevention = models.TextField(max_length=999)
    url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.disease
