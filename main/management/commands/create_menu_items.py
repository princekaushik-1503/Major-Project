from django.core.management.base import BaseCommand
from main.models import MenuItem, Category
from django.core.files import File
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Creates sample menu items'

    def handle(self, *args, **kwargs):
        # Create categories
        categories = {
            'starters': Category.objects.get_or_create(name='Starters')[0],
            'main_courses': Category.objects.get_or_create(name='Main Courses')[0],
            'desserts': Category.objects.get_or_create(name='Desserts')[0],
            'wines': Category.objects.get_or_create(name='Fine Wines')[0],
        }

        # Sample menu items
        menu_items = [
            {
                'name': 'Garlic Bread',
                'description': 'Crispy bread topped with garlic butter and herbs',
                'price': 150,
                'category': categories['starters'],
                'image': 'menu/garlic_bread.jpg'
            },
            {
                'name': 'Caesar Salad',
                'description': 'Fresh romaine lettuce with Caesar dressing, croutons, and parmesan',
                'price': 200,
                'category': categories['starters'],
                'image': 'menu/caesar_salad.jpg'
            },
            {
                'name': 'Grilled Salmon',
                'description': 'Fresh salmon fillet grilled to perfection with lemon butter sauce',
                'price': 450,
                'category': categories['main_courses'],
                'image': 'menu/grilled_salmon.jpg'
            },
            {
                'name': 'Beef Steak',
                'description': 'Premium beef steak cooked to your preference with mushroom sauce',
                'price': 600,
                'category': categories['main_courses'],
                'image': 'menu/beef_steak.jpg'
            },
            {
                'name': 'Chocolate Cake',
                'description': 'Rich chocolate cake with ganache and fresh berries',
                'price': 180,
                'category': categories['desserts'],
                'image': 'menu/chocolate_cake.jpg'
            },
            {
                'name': 'Tiramisu',
                'description': 'Classic Italian dessert with coffee-soaked ladyfingers and mascarpone',
                'price': 200,
                'category': categories['desserts'],
                'image': 'menu/tiramisu.jpg'
            },
            {
                'name': 'Cabernet Sauvignon',
                'description': 'Full-bodied red wine with rich dark fruit flavors',
                'price': 800,
                'category': categories['wines'],
                'image': 'menu/cabernet.jpg'
            },
            {
                'name': 'Chardonnay',
                'description': 'Crisp white wine with notes of apple and vanilla',
                'price': 750,
                'category': categories['wines'],
                'image': 'menu/chardonnay.jpg'
            }
        ]

        # Create menu items
        for item_data in menu_items:
            menu_item, created = MenuItem.objects.get_or_create(
                name=item_data['name'],
                defaults={
                    'description': item_data['description'],
                    'price': item_data['price'],
                    'category': item_data['category']
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created menu item: {menu_item.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Menu item already exists: {menu_item.name}')) 