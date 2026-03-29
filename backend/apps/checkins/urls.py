from django.urls import path

from .views import CheckInCreateAPIView

urlpatterns = [
    path("", CheckInCreateAPIView.as_view(), name="checkin-create"),
]
