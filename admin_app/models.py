from django.contrib.auth.models import User
from django.db import models

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_super_admin = models.BooleanField(default=False)
    can_manage_users = models.BooleanField(default=False)
    can_manage_products = models.BooleanField(default=False)
    can_manage_orders = models.BooleanField(default=False)
    can_manage_reports = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Admin Profile"

class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    can_view_users = models.BooleanField(default=False)
    can_create_users = models.BooleanField(default=False)
    can_update_users = models.BooleanField(default=False)
    can_delete_users = models.BooleanField(default=False)

    can_view_products = models.BooleanField(default=False)
    can_create_products = models.BooleanField(default=False)
    can_update_products = models.BooleanField(default=False)
    can_delete_products = models.BooleanField(default=False)

    can_view_orders = models.BooleanField(default=False)
    can_create_orders = models.BooleanField(default=False)
    can_update_orders = models.BooleanField(default=False)
    can_delete_orders = models.BooleanField(default=False)

    can_view_reports = models.BooleanField(default=False)
    can_generate_reports = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Permissions"

# Create your models here.
