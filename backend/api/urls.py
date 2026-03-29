from django.urls import path
from . import views

urlpatterns = [
    # Primary routes (used by Postman / internal)
    path('checkin', views.create_checkin, name='checkin'),
    path('user/<int:user_id>/risk-history', views.user_risk_history, name='user_risk_history'),
    path('anchors', views.get_anchors, name='anchors'),
    path('session/book', views.book_session, name='book_session'),

    # Frontend-expected aliases
    path('check-in', views.create_checkin, name='check_in_alias'),
    path('anchors/match', views.get_matched_anchor, name='anchors_match'),
    path('sessions/book', views.book_session, name='sessions_book_alias'),
    path('sessions/slots', views.get_slots, name='sessions_slots'),
    path('onboarding', views.save_onboarding, name='onboarding'),
]
