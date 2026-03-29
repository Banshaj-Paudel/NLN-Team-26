from django.urls import path

from .views import AnchorListAPIView, AnchorMatchAPIView

urlpatterns = [
    path("match", AnchorMatchAPIView.as_view(), name="anchors-match"),
    path("", AnchorListAPIView.as_view(), name="anchors-list"),
]
