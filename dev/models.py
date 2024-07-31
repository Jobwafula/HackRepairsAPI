from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Screen(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    status = models.CharField(max_length=20, default='active')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class ScreenElement(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='elements')
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=200)
    panel_type = models.CharField(max_length=200)
    width = models.IntegerField()
    height = models.IntegerField()
    resolution = models.IntegerField()
    position = models.IntegerField()
    category = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.screen.name} - {self.name}"

class ScreenAction(models.Model):
    screen_element = models.ForeignKey(ScreenElement, on_delete=models.CASCADE, related_name='actions')
    action_type = models.CharField(max_length=50)
    action = models.JSONField(blank=True, null=True)
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.screen_element.name} - {self.action_type}"

class UserInteraction(models.Model):
    screen_element = models.ForeignKey(ScreenElement, on_delete=models.CASCADE, related_name='interactions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=now)
    session = models.CharField(max_length=100, blank=True, null=True)
    device_type = models.CharField(max_length=50, blank=True, null=True)
    additional_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.screen_element.name} - {self.interaction_type}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    shipping_address = models.CharField(max_length=200)
    payment_method = models.IntegerField()
    payment_status = models.CharField(max_length=20, default='pending')
    order_status = models.CharField(max_length=50, default='placed')
    delivery_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Order #{self.id}"