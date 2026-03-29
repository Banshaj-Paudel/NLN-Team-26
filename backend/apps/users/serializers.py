from rest_framework import serializers

from apps.checkins.models import CheckIn


class RiskHistoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ["date", "risk_score"]
