from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'admin'
    USER = 'user'


class User(AbstractUser):
    phone = models.CharField(max_length=12)
    role = models.CharField(max_length=5, choices=UserRole.choices, default=UserRole.USER)
