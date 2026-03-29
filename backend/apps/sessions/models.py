from django.conf import settings
from django.db import models

from apps.anchors.models import Anchor


class AnchorSession(models.Model):
    STATUS_BOOKED = "booked"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_BOOKED, "Booked"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="anchor_sessions")
    anchor = models.ForeignKey(Anchor, on_delete=models.CASCADE, related_name="sessions")
    scheduled_for = models.DateTimeField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_BOOKED)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["scheduled_for"]

    def __str__(self) -> str:
        return f"Session(user={self.user_id}, anchor={self.anchor_id}, when={self.scheduled_for})"
