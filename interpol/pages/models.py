from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.TextField(default='admin')
    surname = models.TextField(default='admin')
    age = models.PositiveIntegerField(default=10)
    post = models.TextField()