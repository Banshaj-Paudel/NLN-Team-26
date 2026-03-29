from django.db import models


class Anchor(models.Model):
    name = models.CharField(max_length=120)
    specialty = models.CharField(max_length=120)
    bio = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.specialty})"
