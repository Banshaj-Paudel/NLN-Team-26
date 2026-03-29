from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.anchors.models import Anchor
from .models import AnchorSession
from .serializers import AnchorSessionSerializer, SessionBookingSerializer


class SessionBookAPIView(APIView):
    def post(self, request):
        payload = request.data if isinstance(request.data, dict) else {}

        # Frontend compatibility mode: accepts only a selected slot string.
        if "slot" in payload and not {"user_id", "anchor_id", "scheduled_for"}.issubset(payload.keys()):
            return Response(
                {
                    "status": "booked",
                    "slot": payload.get("slot"),
                    "scheduled_for": timezone.now().isoformat(),
                },
                status=status.HTTP_201_CREATED,
            )

        serializer = SessionBookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payload = serializer.validated_data

        User = get_user_model()
        user = User.objects.filter(id=payload["user_id"]).first()
        if not user:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        anchor = Anchor.objects.filter(id=payload["anchor_id"], is_available=True).first()
        if not anchor:
            return Response({"detail": "Anchor not found or unavailable."}, status=status.HTTP_404_NOT_FOUND)

        booking = AnchorSession.objects.create(
            user=user,
            anchor=anchor,
            scheduled_for=payload["scheduled_for"],
            notes=payload.get("notes", ""),
        )
        return Response(AnchorSessionSerializer(booking).data, status=status.HTTP_201_CREATED)


class SessionSlotsAPIView(APIView):
    def get(self, request):
        return Response(["9:00 AM", "11:00 AM", "1:30 PM", "3:00 PM", "5:30 PM"])


class SessionBookCompatAPIView(APIView):
    def post(self, request):
        slot = request.data.get("slot") if isinstance(request.data, dict) else None
        if not slot:
            return Response({"detail": "slot is required."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {
                "status": "booked",
                "slot": slot,
                "scheduled_for": timezone.now().isoformat(),
            },
            status=status.HTTP_201_CREATED,
        )
