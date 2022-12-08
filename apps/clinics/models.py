from django.contrib.auth.models import models
from django.db import models

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

class Clinics(SoftDeleteModel):
    clinic_name = models.TextField(unique=True)
    clinic_address = models.TextField()
    clinic_mobile = models.TextField()
    clinic_landline = models.TextField()
    clinic_email = models.TextField()
    url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clinic_name