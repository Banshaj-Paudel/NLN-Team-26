from rest_framework import serializers

from .models import CheckIn


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = [
            "id",
            "user",
            "date",
            "mood",
            "stress_level",
            "notes",
            "risk_score",
            "created_at",
        ]
        read_only_fields = ["risk_score", "created_at"]


class CheckInCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    mood = serializers.IntegerField(min_value=1, max_value=10)
    stress_level = serializers.IntegerField(min_value=1, max_value=10)
    notes = serializers.CharField(required=False, allow_blank=True)
    date = serializers.DateField(required=False)
