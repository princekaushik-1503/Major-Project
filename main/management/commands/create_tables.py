from django.core.management.base import BaseCommand
from main.models import Table

class Command(BaseCommand):
    help = 'Creates sample tables for the restaurant'

    def handle(self, *args, **kwargs):
        tables = [
            {
                'name': 'Window Table 1',
                'capacity': 2,
                'category': 'window',
                'is_available': True
            },
            {
                'name': 'Window Table 2',
                'capacity': 4,
                'category': 'window',
                'is_available': True
            },
            {
                'name': 'Private Room 1',
                'capacity': 6,
                'category': 'private',
                'is_available': True
            },
            {
                'name': 'Private Room 2',
                'capacity': 8,
                'category': 'private',
                'is_available': True
            },
            {
                'name': 'Main Dining 1',
                'capacity': 4,
                'category': 'main',
                'is_available': True
            },
            {
                'name': 'Main Dining 2',
                'capacity': 4,
                'category': 'main',
                'is_available': True
            },
            {
                'name': 'Outdoor Table 1',
                'capacity': 2,
                'category': 'outdoor',
                'is_available': True
            },
            {
                'name': 'Outdoor Table 2',
                'capacity': 4,
                'category': 'outdoor',
                'is_available': True
            }
        ]

        for table_data in tables:
            Table.objects.get_or_create(
                name=table_data['name'],
                defaults=table_data
            )
            self.stdout.write(self.style.SUCCESS(f'Created table: {table_data["name"]}')) 