from django.urls import path

from .views import UserRiskHistoryAPIView

urlpatterns = [
    path("<int:user_id>/risk-history", UserRiskHistoryAPIView.as_view(), name="user-risk-history"),
]
