from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    tax_rate = models.SmallIntegerField(default=10)

    sign_image = models.ImageField(upload_to='user-signs/', blank=True, null=True)
