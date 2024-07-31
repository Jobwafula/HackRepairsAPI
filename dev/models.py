from django.db import models
from django.utils.timezone import now

class Screen(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class ScreenElement(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='elements')
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=200, blank=True, null=True)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.screen.name} - {self.name}"

class ScreenAction(models.Model):
    screen_element = models.ForeignKey(ScreenElement, on_delete=models.CASCADE, related_name='actions')
    action_type = models.CharField(max_length=50)
    action_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.screen_element.name} - {self.action_type}"

class UserInteraction(models.Model):
    screen_element = models.ForeignKey(ScreenElement, on_delete=models.CASCADE, related_name='interactions')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=now)
    additional_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.screen_element.name} - {self.interaction_type}"