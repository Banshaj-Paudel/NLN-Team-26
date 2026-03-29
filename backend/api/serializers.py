from rest_framework import serializers
from .models import Anchor, CheckIn, Session
from users.serializers import UserSerializer

class AnchorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anchor
        fields = '__all__'

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = '__all__'
        read_only_fields = ['user']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
        read_only_fields = ['user', 'anchor']
