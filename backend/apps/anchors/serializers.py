from rest_framework import serializers

from .models import Anchor


class AnchorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anchor
        fields = ["id", "name", "specialty", "bio", "is_available", "rating"]
