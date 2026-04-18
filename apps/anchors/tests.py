from django.test import TestCase
from rest_framework.test import APIClient

from .models import Anchor


class AnchorMatchSecurityTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_anchor_match_sanitizes_dynamic_anchor_content(self):
        Anchor.objects.create(
            name="<script>alert(1)</script><b>Eve</b>",
            specialty="<img src=x onerror=alert(1)>Career",
            bio="<script>alert(1)</script>Trusted <i>mentor</i>",
            is_available=True,
        )

        response = self.client.get("/anchors/match")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Eve")
        self.assertEqual(response.data["role"], "Career")
        self.assertEqual(response.data["story"], "Trusted mentor")
        self.assertTrue(all("<" not in tag for tag in response.data["tags"]))
