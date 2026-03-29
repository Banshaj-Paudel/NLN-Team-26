from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Anchor

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with mock users and anchors'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')
        
        # Create users
        for i in range(1, 6):
            User.objects.get_or_create(
                username=f'user{i}',
                defaults={
                    'name': f'Mock User {i}',
                    'career_stage': 'Final year CS',
                    'stressor_tags': ['Job rejection', 'Startup stress'],
                    'risk_level': 'Amber'
                }
            )
        
        # Create anchors
        anchors_data = [
            {"name": "Alice Johnson", "tags": ["Software Engineer", "Burnout Survivor"]},
            {"name": "Bob Smith", "tags": ["Product Manager", "Career Transition"]},
            {"name": "Charlie Davis", "tags": ["Final year CS", "Job rejection"]},
            {"name": "Diana Ross", "tags": ["Startup stress", "Founder"]},
        ]
        
        for data in anchors_data:
            Anchor.objects.get_or_create(
                name=data['name'],
                defaults={
                    'background_tags': data['tags'],
                    'availability': {"monday": ["10:00", "14:00"], "wednesday": ["16:00"]}
                }
            )
            
        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
