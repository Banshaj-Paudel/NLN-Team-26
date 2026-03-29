from django.contrib import admin

from .models import AnchorSession


@admin.register(AnchorSession)
class AnchorSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "anchor", "scheduled_for", "status", "created_at")
    list_filter = ("status", "scheduled_for", "created_at")
    search_fields = ("user__username", "user__email", "anchor__name", "notes")
