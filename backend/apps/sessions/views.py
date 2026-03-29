from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.anchors.models import Anchor
from .models import AnchorSession
from .serializers import AnchorSessionSerializer, SessionBookingSerializer


class SessionBookAPIView(APIView):
    def post(self, request):
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
