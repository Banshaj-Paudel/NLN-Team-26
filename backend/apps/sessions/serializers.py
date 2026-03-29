from rest_framework import serializers

from .models import AnchorSession


class SessionBookingSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    anchor_id = serializers.IntegerField()
    scheduled_for = serializers.DateTimeField()
    notes = serializers.CharField(required=False, allow_blank=True)


class AnchorSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnchorSession
        fields = ["id", "user", "anchor", "scheduled_for", "status", "notes", "created_at"]
        read_only_fields = ["status", "created_at"]
