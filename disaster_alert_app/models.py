from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    last_access = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: ({self.latitude}, {self.longitude}) at {self.last_access}"

class Disaster(models.Model):
    HIGH = 'h'
    MEDIUM = 'm'
    LOW = 'l'

    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)

    def __str__(self):
        return f"{self.description} ({self.priority}) ({self.latitude}, {self.longitude})"
