
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username
    

class Business(models.Model):
    name = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    business_location = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    product = models.CharField(max_length=50)

    def __str__(self):
        return self.name