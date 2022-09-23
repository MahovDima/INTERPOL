from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=10)
    post = models.TextField()