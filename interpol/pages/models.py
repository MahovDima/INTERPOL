from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=10)
    post = models.TextField(default='User')

class SecretCodes(models.Model):
    code = models.TextField()
    def __str__(self):
        return self.code

class WantedPersons(models.Model):
    name = models.TextField()
    age = models.TextField()
    briefInfo = models.TextField()
    photo = models.ImageField(upload_to='wanted/', default=None)
    detailInfo = models.TextField()
    isPublished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

