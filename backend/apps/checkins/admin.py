from django.contrib import admin

from .models import CheckIn


@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "mood", "stress_level", "risk_score", "created_at")
    list_filter = ("date", "created_at")
    search_fields = ("user__username", "user__email", "notes")
