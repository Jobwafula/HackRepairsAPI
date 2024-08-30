
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    username = None
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number']

    def __str__(self):
        return f" {self.full_name} ({self.email})"
    

class Business(models.Model):
    name = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    business_location = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    product = models.CharField(max_length=50)

    def __str__(self):
        return self.name