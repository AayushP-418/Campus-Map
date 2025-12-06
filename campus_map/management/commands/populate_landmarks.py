from django.core.management.base import BaseCommand
from campus_map.models import Landmark


class Command(BaseCommand):
    help = 'Populates the database with default Georgia Tech landmarks'

    def handle(self, *args, **options):
        landmarks_data = [
            {
                'name': 'Tech Tower',
                'latitude': 33.7718,
                'longitude': -84.3944,
                'description': 'The iconic Tech Tower, the main administrative building of Georgia Tech.',
            },
            {
                'name': 'Bobby Dodd Stadium',
                'latitude': 33.7725,
                'longitude': -84.3929,
                'description': 'Home of the Georgia Tech Yellow Jackets football team.',
            },
            {
                'name': 'Klaus Advanced Computing Building',
                'latitude': 33.7772,
                'longitude': -84.3963,
                'description': 'State-of-the-art computing facility housing the College of Computing.',
            },
            {
                'name': 'Student Center',
                'latitude': 33.7740,
                'longitude': -84.3988,
                'description': 'The heart of student life with dining, events, and student services.',
            },
            {
                'name': 'Library',
                'latitude': 33.7743,
                'longitude': -84.3958,
                'description': 'Price Gilbert Library - the main library on campus.',
            },
            {
                'name': 'Campus Recreation Center',
                'latitude': 33.7755,
                'longitude': -84.4040,
                'description': 'CRC - Campus recreation and fitness facility.',
            },
            {
                'name': 'Clough Undergraduate Learning Commons',
                'latitude': 33.7748,
                'longitude': -84.3964,
                'description': 'CULC - Modern study and collaboration space for students.',
            },
            {
                'name': 'Tech Green',
                'latitude': 33.7745,
                'longitude': -84.3973,
                'description': 'The central green space on campus, a popular gathering area.',
            },
        ]

        created_count = 0
        updated_count = 0

        for landmark_data in landmarks_data:
            landmark, created = Landmark.objects.get_or_create(
                name=landmark_data['name'],
                defaults={
                    'latitude': landmark_data['latitude'],
                    'longitude': landmark_data['longitude'],
                    'description': landmark_data['description'],
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created: {landmark.name}')
                )
            else:
                # Update existing landmark if coordinates or description changed
                updated = False
                if str(landmark.latitude) != str(landmark_data['latitude']):
                    landmark.latitude = landmark_data['latitude']
                    updated = True
                if str(landmark.longitude) != str(landmark_data['longitude']):
                    landmark.longitude = landmark_data['longitude']
                    updated = True
                if landmark.description != landmark_data['description']:
                    landmark.description = landmark_data['description']
                    updated = True
                
                if updated:
                    landmark.save()
                    updated_count += 1
                    self.stdout.write(
                        self.style.WARNING(f'↻ Updated: {landmark.name}')
                    )
                else:
                    self.stdout.write(
                        self.style.NOTICE(f'○ Already exists: {landmark.name}')
                    )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✓ Successfully populated landmarks! '
                f'Created: {created_count}, Updated: {updated_count}'
            )
        )

