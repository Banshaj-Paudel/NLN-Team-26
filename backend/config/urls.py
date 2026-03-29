from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("checkin", include("apps.checkins.urls")),
    path("user/", include("apps.users.urls")),
    path("anchors", include("apps.anchors.urls")),
    path("session/", include("apps.sessions.urls")),
]
