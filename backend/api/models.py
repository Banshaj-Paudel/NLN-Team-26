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
    mood_source = models.CharField(max_length=50, default="self_report")
    tasks_done = models.IntegerField(default=0)
    tasks_planned = models.IntegerField(default=0)
    tasks_completion_rate = models.FloatField(default=0.0)
    days_in_stress = models.IntegerField(default=0)
    journal_text = models.TextField(blank=True)

    def __str__(self):
        user_name = self.user.username or self.user.name or f"User {self.user.id}"
        return f"{user_name} - {self.date}"

class BurnMapResult(models.Model):
    checkin = models.OneToOneField(CheckIn, on_delete=models.CASCADE, related_name='burnmap_result')
    risk_level = models.CharField(max_length=10)
    score = models.IntegerField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user_name = self.checkin.user.username or self.checkin.user.name or f"User {self.checkin.user.id}"
        return f"BurnMapResult: {user_name} - {self.checkin.date}"

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
