from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy
from django.db import models

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey("Role", on_delete=models.CASCADE, default=1)

class SecretCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.TextField()
    role = models.ForeignKey("Role", on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.code

class WantedPerson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    age = models.TextField()
    briefInfo = models.TextField()
    photo = models.ImageField(upload_to='wanted/', default=None)
    detailInfo = models.TextField()
    authorId = models.ForeignKey("CustomUser", on_delete=models.CASCADE, default=1)
    isPublished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.TextField(default='User')

    def __str__(self):
        return self.role
