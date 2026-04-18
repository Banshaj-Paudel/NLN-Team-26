from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.checkins.models import CheckIn
from apps.security import sanitize_text
from .serializers import RiskHistoryItemSerializer


class UserRiskHistoryAPIView(APIView):
    def get(self, request, user_id: int):
        User = get_user_model()
        if not User.objects.filter(id=user_id).exists():
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        since = timezone.localdate() - timedelta(days=6)
        checkins = (
            CheckIn.objects.filter(user_id=user_id, date__gte=since)
            .order_by("date")
        )
        serializer = RiskHistoryItemSerializer(checkins, many=True)
        return Response({"user_id": user_id, "history": serializer.data}, status=status.HTTP_200_OK)


class OnboardingSaveAPIView(APIView):
    def post(self, request):
        payload = request.data if isinstance(request.data, dict) else {}
        received = {
            "name": sanitize_text(payload.get("name"), max_length=150),
            "careerStage": sanitize_text(payload.get("careerStage"), max_length=120),
            "stressor": sanitize_text(payload.get("stressor"), max_length=80),
        }
        return Response({"ok": True, "received": received}, status=status.HTTP_200_OK)
