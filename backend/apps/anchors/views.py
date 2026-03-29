from rest_framework import generics

from .models import Anchor
from .serializers import AnchorSerializer


class AnchorListAPIView(generics.ListAPIView):
    queryset = Anchor.objects.filter(is_available=True).order_by("name")
    serializer_class = AnchorSerializer
