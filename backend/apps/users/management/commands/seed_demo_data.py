import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from apps.anchors.models import Anchor


class Command(BaseCommand):
    help = "Seed demo users and anchor profiles"

    def handle(self, *args, **kwargs):
        user_names = [
            "alex", "jamie", "sam", "taylor", "casey", "morgan", "riley", "jordan"
        ]
        specialties = [
            "Anxiety Support",
            "Burnout Recovery",
            "Career Clarity",
            "Stress Management",
            "Work-Life Balance",
            "Mindfulness",
            "Confidence Coaching",
            "Relationship Support",
            "Sleep Reset",
            "Resilience Building",
            "Focus Coaching",
            "Life Transitions",
            "Habit Building",
            "Emotional Regulation",
            "Goal Planning",
        ]

        User = get_user_model()
        created_users = 0
        for name in user_names[:5]:
            _, created = User.objects.get_or_create(
                username=name,
                defaults={
                    "email": f"{name}@demo.com",
                },
            )
            if created:
                created_users += 1

        created_anchors = 0
        for idx, specialty in enumerate(specialties[:12], start=1):
            _, created = Anchor.objects.get_or_create(
                name=f"Anchor {idx}",
                defaults={
                    "specialty": specialty,
                    "bio": f"Guides people through {specialty.lower()} with practical weekly steps.",
                    "is_available": True,
                    "rating": round(random.uniform(4.2, 5.0), 2),
                },
            )
            if created:
                created_anchors += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed complete. New users: {created_users}, new anchors: {created_anchors}"
            )
        )
