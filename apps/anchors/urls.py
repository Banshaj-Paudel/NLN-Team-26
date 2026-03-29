from django.urls import path

from .views import AnchorListAPIView

urlpatterns = [
    path("", AnchorListAPIView.as_view(), name="anchors-list"),
]
