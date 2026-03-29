from django.urls import path

from .views import SessionBookAPIView

urlpatterns = [
    path("book", SessionBookAPIView.as_view(), name="session-book"),
]
