from django.contrib.auth.models import models
from datetime import datetime

from ..user.models import User
from ..diseases.models import Diseases

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


class Results(SoftDeleteModel):
    user = models.ForeignKey(User, verbose_name="User", blank=True, null=True, on_delete=models.CASCADE)
    disease = models.TextField(max_length=999)
    confidence = models.FloatField(max_length=1)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.disease
