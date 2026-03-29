from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    career_stage = models.CharField(max_length=100, blank=True)
    stressor_tags = models.JSONField(default=list, blank=True)
    
    RISK_LEVEL_CHOICES = [
        ('Green', 'Green'),
        ('Amber', 'Amber'),
        ('Red', 'Red'),
    ]
    risk_level = models.CharField(max_length=20, default='Green', choices=RISK_LEVEL_CHOICES)

    def __str__(self):
        return self.username or self.name
