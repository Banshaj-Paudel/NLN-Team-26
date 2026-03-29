from django.conf import settings
from django.db import models
from django.utils import timezone


class CheckIn(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="checkins")
    date = models.DateField(default=timezone.localdate)
    mood = models.IntegerField()
    stress_level = models.IntegerField()
    notes = models.TextField(blank=True)
    risk_score = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "date")
        ordering = ["-date", "-created_at"]

    def __str__(self) -> str:
        return f"CheckIn(user={self.user_id}, date={self.date}, risk={self.risk_score})"
