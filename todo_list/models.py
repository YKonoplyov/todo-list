from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=255)