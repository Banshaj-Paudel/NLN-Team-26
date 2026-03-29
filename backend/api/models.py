from django.db import models
from django.conf import settings

class Anchor(models.Model):
    name = models.CharField(max_length=255)
    background_tags = models.JSONField(default=list, blank=True)
    availability = models.JSONField(default=dict, blank=True)
    matched_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class CheckIn(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='checkins')
    date = models.DateField(auto_now_add=True)
    sleep_hours = models.FloatField()
    mood_score = models.IntegerField()  # 1 to 5
    tasks_done = models.IntegerField(default=0)
    journal_text = models.TextField(blank=True)

    def __str__(self):
        user_name = self.user.username or self.user.name or f"User {self.user.id}"
        return f"{user_name} - {self.date}"

class Session(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sessions_as_user')
    anchor = models.ForeignKey(Anchor, on_delete=models.CASCADE, related_name='sessions_as_anchor')
    scheduled_at = models.DateTimeField()
    
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')

    def __str__(self):
        user_name = self.user.username or self.user.name or f"User {self.user.id}"
        return f"Session: {user_name} with {self.anchor.name}"
