from django.test import TestCase
from rest_framework.test import APIClient


class SessionBookingSecurityTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_sessions_book_compatibility_response_sanitizes_slot(self):
        response = self.client.post(
            "/sessions/book",
            {"slot": '<img src=x onerror=alert(1)>9:00 AM'},
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["slot"], "9:00 AM")

    def test_sessions_book_compat_endpoint_sanitizes_slot(self):
        response = self.client.post(
            "/sessions/book-compat",
            {"slot": "<script>alert(1)</script>11:00 AM"},
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["slot"], "11:00 AM")
