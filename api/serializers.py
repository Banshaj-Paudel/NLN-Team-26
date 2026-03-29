from rest_framework import serializers
from .models import Anchor, BurnMapResult, CheckIn, Session
from users.serializers import UserSerializer

class AnchorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anchor
        fields = '__all__'

class CheckInSerializer(serializers.ModelSerializer):
    tasks_completed_percent = serializers.SerializerMethodField()

    class Meta:
        model = CheckIn
        fields = '__all__'
        read_only_fields = ['user']

    def get_tasks_completed_percent(self, obj):
        return int(round(obj.tasks_completion_rate * 100))

class BurnMapResultSerializer(serializers.ModelSerializer):
    risk_level_display = serializers.SerializerMethodField()

    class Meta:
        model = BurnMapResult
        fields = '__all__'
        read_only_fields = ['checkin']

    def get_risk_level_display(self, obj):
        return obj.risk_level.upper()

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
        read_only_fields = ['user', 'anchor']
