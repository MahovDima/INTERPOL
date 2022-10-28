from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy
from django.db import models

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    age = models.PositiveIntegerField(default=10)
    post = models.TextField(default='User')

class SecretCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.TextField()
    post = models.PositiveIntegerField()
    def __str__(self):
        return self.code

class WantedPerson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    age = models.TextField()
    briefInfo = models.TextField()
    photo = models.ImageField(upload_to='wanted/', default=None)
    detailInfo = models.TextField()
    isPublished = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    author = models.TextField()
    post = models.IntegerField()

    def __str__(self):
        return self.text
