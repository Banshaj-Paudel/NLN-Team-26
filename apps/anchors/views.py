from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.security import sanitize_text, sanitize_text_list
from .models import Anchor
from .serializers import AnchorSerializer


class AnchorListAPIView(generics.ListAPIView):
    queryset = Anchor.objects.filter(is_available=True).order_by("name")
    serializer_class = AnchorSerializer


class AnchorMatchAPIView(APIView):
    def get(self, request):
        anchor = Anchor.objects.filter(is_available=True).order_by("-rating", "name").first()
        if not anchor:
            return Response(
                {
                    "name": "Support Anchor",
                    "role": "Peer Mentor",
                    "story": "A trained peer is ready to support your burnout recovery plan.",
                    "tags": ["Burnout support"],
                    "initials": "SA",
                }
            )

        name_parts = [part for part in anchor.name.split() if part]
        initials = "".join(part[0].upper() for part in name_parts[:2]) or "AN"
        specialty = sanitize_text(anchor.specialty, max_length=120) or "Peer Mentor"
        return Response(
            {
                "name": sanitize_text(anchor.name, max_length=120),
                "role": specialty,
                "story": sanitize_text(
                    anchor.bio or "Experienced mentor with practical burnout recovery strategies.",
                    max_length=500,
                ),
                "tags": sanitize_text_list([specialty, "Burnout support"], max_items=2, item_max_length=80),
                "initials": sanitize_text(initials, max_length=4),
            }
        )
