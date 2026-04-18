from django.test import TestCase
from rest_framework.test import APIClient


class OnboardingSaveSecurityTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_onboarding_response_sanitizes_html_and_scripts(self):
        response = self.client.post(
            "/onboarding",
            {
                "name": "<script>alert(1)</script><b>Alice</b>",
                "careerStage": "<i>Graduate</i>",
                "stressor": '"><img src=x onerror=alert(1)>',
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["received"]["name"], "Alice")
        self.assertEqual(response.data["received"]["careerStage"], "Graduate")
        self.assertNotIn("<", response.data["received"]["stressor"])
