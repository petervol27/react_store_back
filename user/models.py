from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.username
