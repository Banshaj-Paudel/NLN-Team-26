from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

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
        return Response(
            {
                "name": anchor.name,
                "role": anchor.specialty,
                "story": anchor.bio or "Experienced mentor with practical burnout recovery strategies.",
                "tags": [anchor.specialty, "Burnout support"],
                "initials": initials,
            }
        )
