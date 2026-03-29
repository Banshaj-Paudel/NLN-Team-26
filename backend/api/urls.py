from django.urls import path
from . import views

urlpatterns = [
    path('checkin', views.create_checkin, name='checkin'),
    path('user/<int:user_id>/risk-history', views.user_risk_history, name='user_risk_history'),
    path('anchors', views.get_anchors, name='anchors'),
    path('session/book', views.book_session, name='book_session'),
]
