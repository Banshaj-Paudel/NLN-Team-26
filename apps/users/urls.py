from django.urls import path

from .views import OnboardingSaveAPIView, UserRiskHistoryAPIView

urlpatterns = [
    path("onboarding", OnboardingSaveAPIView.as_view(), name="onboarding-save"),
    path("<int:user_id>/risk-history", UserRiskHistoryAPIView.as_view(), name="user-risk-history"),
]
