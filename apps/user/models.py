from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_inactive = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_staff']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

