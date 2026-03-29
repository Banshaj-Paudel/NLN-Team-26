from django.urls import path

from .views import SessionBookAPIView, SessionBookCompatAPIView, SessionSlotsAPIView

urlpatterns = [
    path("book", SessionBookAPIView.as_view(), name="session-book"),
    path("slots", SessionSlotsAPIView.as_view(), name="session-slots"),
    path("book-compat", SessionBookCompatAPIView.as_view(), name="session-book-compat"),
]
