from django.contrib import admin

from .models import Anchor


@admin.register(Anchor)
class AnchorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "specialty", "is_available", "rating", "created_at")
    list_filter = ("is_available", "specialty")
    search_fields = ("name", "specialty")
