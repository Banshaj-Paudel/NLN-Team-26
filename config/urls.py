from django.contrib import admin
from django.urls import include, path
from apps.users.views import OnboardingSaveAPIView
from apps.sessions.views import SessionBookCompatAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("checkin", include("apps.checkins.urls")),
    path("check-in", include("apps.checkins.urls")),
    path("checkin/", include("apps.checkins.urls")),
    path("check-in/", include("apps.checkins.urls")),
    path("user/", include("apps.users.urls")),
    path("anchors", include("apps.anchors.urls")),
    path("anchors/", include("apps.anchors.urls")),
    path("session/", include("apps.sessions.urls")),
    path("sessions/", include("apps.sessions.urls")),
    path("sessions/book", SessionBookCompatAPIView.as_view(), name="session-book-frontend"),
    path("sessions/book/", SessionBookCompatAPIView.as_view(), name="session-book-frontend-slash"),
    path("onboarding", OnboardingSaveAPIView.as_view(), name="onboarding-root"),
    path("onboarding/", OnboardingSaveAPIView.as_view(), name="onboarding-root-slash"),
]
